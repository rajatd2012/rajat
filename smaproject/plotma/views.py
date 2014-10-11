from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
import numpy as np
import matplotlib.colors as colors
import matplotlib.finance as finance
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as font_manager

# Create your views here.

def index(request):
    
    Nifty5d1min = pd.read_csv('http://www.google.com/finance/getprices?q=.NSEI&x=NSE&i=60&p=5d&f=d,o,h,l,c,v',skiprows =8)
    pd.DataFrame.plot(Nifty5d1min.ix[:,1:2],title="Nifty5d1min",ylim=[7800,8200],legend=False)
    
    plt.savefig("static/img/Nifty5d1min.png")
    
    context = RequestContext(request)
    return render_to_response('plotma/index.html',{}, context)
