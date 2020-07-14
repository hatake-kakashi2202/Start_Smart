from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool
from .models import finances

from math import pi

import pandas as pd

from bokeh.io import output_file, show
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum
# Create your views here.
def finance(request):
	return render(request, 'finance.html')

def graph(request):
	mod = finances.objects.get(user=request.user)
	exp = mod.Expenditure.split("+")
	tran = mod.income.split("+")
	trans = mod.transactions.split("+")
	exp = [int(i) for i in exp]
	tran = [int(i) for i in tran]
	plot = figure()
	plot.line([1,2,3,4],exp,color='blue')
	plot.line([1,2,3,4],tran,color='red')
	script, div = components(plot)
	x={trans[i]: exp[i] for i in range(len(trans))} 
	data = pd.Series(x).reset_index(name='value').rename(columns={'index':'country'})
	data['angle'] = data['value']/data['value'].sum() * 2*pi
	data['color'] = Category20c[len(x)]

	p = figure(plot_height=350, title="Pie Chart", toolbar_location=None,
			tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

	p.wedge(x=0, y=1, radius=0.4,
			start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
			line_color="white", fill_color='color', legend_field='country', source=data)

	p.axis.axis_label=None
	p.axis.visible=False
	p.grid.grid_line_color = None
	script1, div1 = components(p)
	return render(request,'finance.html',{'script':script,'div':div,'script1':script1,'div1':div1})
