from bokeh.plotting import figure,ColumnDataSource,curdoc
from bokeh.models import DatePicker, WidgetBox, Tabs, Panel
from datetime import date
import pandas as pd
from bokeh.transform import factor_cmap
from bokeh.layouts import row
from bokeh.models import HoverTool, FactorRange, Label


def tab1():
    
    data_cal=pd.read_csv('latimes-state-totals.csv')
    data_cal['date_time']=pd.to_datetime(data_cal['date'])
    data_cal=data_cal[data_cal['date_time'].dt.month==8]
    p=figure(y_axis_label='New Confirmed Cases',title='New Cases California in month of August ',x_axis_type='datetime')
    r=p.line('date_time','new_confirmed_cases',source=data_cal)
    latest_date=max((data_cal['date_time'])).date()
    p.add_tools(HoverTool(
            tooltips=[
                    ('date','@date_time{%Y-%m-%d}'),
                    ('new cases','@new_confirmed_cases'),
                    ],
            formatters={
                    '@date_time':'datetime',
                    }))
    
    metadata = Label(x=21, y=-100, x_units='screen', text="Source for the data: latimes-state-totals.csv " f"Date of last update: {latest_date}",render_mode='css')
    
    p.add_layout(metadata)
    tab = Panel(child=p, title='Number of new coronavirus cases in California in August')
    return tab
    
def tab2():
    data_cas = pd.read_csv('cdph-race-ethnicity.csv')
    data_cas['date_time'] = pd.to_datetime(data_cas['date'])
    data_cas = data_cas[(data_cas['age'] == 'all')]
    cols = ['confirmed_cases_percent', 'population_percent']
    races = ['asian', 'black', "cdph-other", 'latino', 'other', 'white'] ## getting the order from the dataframe
    x = [(j, i) for j in races for i in cols]
    max_date=max((data_cas['date_time'])).date()
    def create_dataset_tab2(df):
        counts = sum(zip(df['confirmed_cases_percent'], df['population_percent']), ())  
        source = ColumnDataSource(data=dict(x=x, counts=counts))
        return source

    def create_plot_tab2(source):
        p = figure(x_range=FactorRange(*x),title='percent cases by race compared to their representation in the general population',y_axis_label='percentge')
        p.vbar(x='x', top='counts', source=source,fill_color=factor_cmap('x', palette=['red','blue'], factors=cols, start=1, end=2))
        p.y_range.start = 0
        p.xaxis.major_label_orientation = 1
        metadata = Label(x=18, y=-200, x_units='screen',y_units='screen', text="Source of data: cdph-race-ethnicity.csv  " "Date of last update{}".format(max_date),render_mode='css')
        p.add_layout(metadata)
        return p

    def callback(attr, old, new):
        new_src = create_dataset_tab2(data_cas[(data_cas['date_time']==date_picker.value)])
        src.data.update(new_src.data)

    # Initial Plot
    src = create_dataset_tab2(data_cas[(data_cas['date_time']=='2020-05-21')])
    p = create_plot_tab2(src)
    date_picker = DatePicker(title='Please Choose a Date(Default Date Given)', min_date=min((data_cas['date_time'])).date(), max_date=max((data_cas['date_time'])).date(),value='2020-05-21')
    date_picker.on_change('value', callback)
    controls = WidgetBox(date_picker)
    layout = row(controls,p)
    tab = Panel(child=layout, title='Percentage cases by race')
    return tab

def tab3():
    data_death = pd.read_csv('cdph-race-ethnicity.csv')
    data_death['date_time'] = pd.to_datetime(data_death['date'])
    data_death = data_death[(data_death['age'] == 'all')]
    cols = ['deaths_percent', 'population_percent']
    races = ['asian', 'black', "cdph-other", 'latino', 'other', 'white'] ## getting the order from the dataframe
    x = [(j, i) for j in races for i in cols]
    max_date=max((data_death['date_time'])).date()

    def create_dataset_tab3(df):
        counts = sum(zip(df['deaths_percent'], df['population_percent']), ())
        source = ColumnDataSource(data=dict(x=x, counts=counts))
        return source

    def create_plot_tab3(source):
        p = figure(x_range=FactorRange(*x), title='percent deaths by race compared to their representation in the general population',y_axis_label='percentge')
        p.vbar(x='x', top='counts',  source=source,fill_color=factor_cmap('x', palette=['red','blue'], factors=cols, start=1, end=2))
        p.y_range.start = 0
        p.xaxis.major_label_orientation = 1
        metadata = Label(x=18,y=-200, x_units='screen',y_units='screen', text="Source of data: cdph-race-ethnicity.csv " "Date of last update{}".format(max_date),render_mode='css' )
        p.add_layout(metadata)
        return p

    def callback(attr, old, new):
        new_src = create_dataset_tab3(data_death[(data_death['date_time']==date_picker.value)])
        src.data.update(new_src.data)

    
    src = create_dataset_tab3(data_death[(data_death['date_time']=='2020-05-21')])
    p = create_plot_tab3(src)
    date_picker = DatePicker(title='Please Choose a Date(Default Date Given)', min_date=min((data_death['date_time'])).date(), max_date=max((data_death['date_time'])).date(),value='2020-05-21')
    date_picker.on_change('value', callback)
    controls = WidgetBox(date_picker)
    layout = row(controls,p)
    tab = Panel(child=layout, title='Percentage deaths by race')
    return tab

tab1=tab1()
tab2=tab2()
tab3=tab3()
tabs = Tabs(tabs = [tab1,tab2,tab3])
curdoc().add_root(tabs)