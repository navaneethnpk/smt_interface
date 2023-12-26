#Aim: Make plots for triggers (CZTI-0.1,1.0, VETO-1.0)
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import os, glob
plt.rcParams['figure.max_open_warning'] = 0 # Suppress the warning

#Function to make combined lightcurves of VETO and CZTI
def makeplots(triglist, evtpath, plotfolder):
        eobs, eorb, east, eutc = triglist[0], triglist[1], triglist[2], triglist[3]
        evtFile = fits.open(evtpath)

        #Time windows
        ttime = float(east)
        tmin = int(ttime - 100)
        tmax =int(ttime + 100)
        quadLabel = ['A', 'B', 'C', 'D']

        cbin = [0.1, 1.0, 10.0]
        for tb in cbin:
                plt.figure(figsize=(8, 6))
                for qd in range(4):
                        #Read & plot CZT data
                        quadData = evtFile[qd+1].data['Time']
                        cztQuad = quadData[(quadData > tmin) & (quadData < tmax)]
                        ctime = np.arange(tmin, tmax + tb / 100.0, tb)
                        chist, bin_edges = np.histogram(cztQuad, bins=ctime)
                        cplot= 0.5 * (ctime[1:] + ctime[:-1])
                        plt.plot(cplot, chist, label=quadLabel[qd])
                plt.xlabel('Time (Sec)')
                plt.ylabel('Counts/Sec')
                plt.grid(True, alpha=0.3)
                plt.legend()
                plt.xlim(tmin, tmax)
                plt.title('Trigger Plot [{}] [Bin: {}] [CZTI]'.format(east, tb))
                plt.axvline(x=ttime, color='k', linestyle='--')
                plt.savefig('{}/{}_{}_CZTI.png'.format(plotfolder, east, tb))
                # plt.show()

        vbin = [int(1), int(10)] #Veto binning needs to be integer
        for tb in vbin:
                plt.figure(figsize=(8, 6))
                for qd in range(4):
                        #Read & plot VETO data
                        vetoData = evtFile[5].data
                        vetoQuad = vetoData[np.where(evtFile[5].data['QuadID'] == qd)]['VetoSpec'][:,0:128]
                        vetoTime = vetoData[np.where(evtFile[5].data['QuadID'] == qd)]['Time']
                        vetoTime = vetoTime.astype(int)
                        bin_start, bin_end = np.where(vetoTime >= tmin)[0][0], np.where(vetoTime <= tmax)[0][-1]
                        vtime = vetoTime[bin_start:bin_end][0:-1:tb]
                        vetoQuad = np.array(vetoQuad[bin_start:bin_end])
                        hveto = []
                        for i in range(len(vtime)):
                                hveto.append(np.sum(vetoQuad[tb*i:tb*(i+1)],axis=0))
                        hveto = np.array(hveto)
                        vhist = np.nansum(hveto, axis=1) / tb
                        vplot = 0.5 * (vtime[1:] + vtime[:-1])
                        if len(vhist)!=len(vplot):
                                vhist = vhist[:-1]
                        plt.plot(vplot, vhist, label=quadLabel[qd])
                plt.xlabel('Time (Sec)')
                plt.ylabel('Counts/Sec')
                plt.grid(True, alpha=0.3)
                plt.legend()
                plt.xlim(tmin, tmax)
                plt.title('Trigger Plot [{}] [Bin: {}] [VETO]'.format(east, tb))
                plt.axvline(x=ttime, color='k', linestyle='--')
                plt.savefig('{}/{}_{}_VETO.png'.format(plotfolder, east, tb))
                # plt.show()
        
        return

alldata = 'test_data.txt'
with open(alldata, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
datalist = []
for item in lines:
        data = item.split(',')
        datalist.append(data)
for item in datalist:
        evtpath = glob.glob('/data2/czti/level2/{}/czti/orbit/{}/modeM0/*_quad_clean.evt'.format(item[0], item[1]))    
        if evtpath:
                plotfolder = '/data2/czti/testarea/navaneeth/smt_interface/static/{}'.format(item[2])
                if not os.path.exists(plotfolder):
                        os.makedirs(plotfolder)
                makeplots(item, evtpath[0], plotfolder)
                print('Plot created - {}'.format(item))
        else:
                continue
