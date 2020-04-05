# line graph widget
def infection_rates_per_county():
    
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    plt.style.use('fivethirtyeight')
    import ipywidgets as widgets
    from ipywidgets import interact, interactive, fixed, interact_manual
    
    mrsa_merged = pd.read_csv('data/mrsa_merged.csv')
    
    def line_county(county):
        plt.figure(figsize=(10,5));
        x = list(mrsa_merged.loc[mrsa_merged['County']== county].groupby(['Year']).agg(sum).index)
        y = list(mrsa_merged.loc[mrsa_merged['County']== county].groupby(['Year']).agg(sum)['Infection_Count'])
        sns.lineplot(x,y)
        title = 'Infection Count in '+county+' County Per Year'
        plt.title(title)
        plt.xlabel("Year")
        plt.ylabel("Infection Count");
        return 

    wid_1 = widgets.Dropdown(
            options = mrsa_merged['County'].unique().tolist(),
            description = 'County',
            disabled = False
    )

    interact(line_county, county = wid_1);

    
# widget 2
def population_v_infection_by_county():
    
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    plt.style.use('fivethirtyeight')
    import ipywidgets as widgets
    from ipywidgets import interact, interactive, fixed, interact_manual
    
    mrsa_merged = pd.read_csv('data/mrsa_merged.csv')
    infec_pop_merge = pd.read_csv('data/infec_pop_merge.csv')
    
    def pop_v_infec_by_county(county):    
        df = infec_pop_merge.loc[infec_pop_merge['County'] == county]  
        p = sns.lmplot(x='Year',y='Infec_Div_Pop',data=df,ci=None,height=6,aspect=2)
        title = 'Infection Count Per 100,000 People in '+county+' County'
        plt.title(title)
        plt.xlabel("Year")
        plt.ylabel("Infection Rate")
        plt.setp(p.ax.lines,linewidth=2)

        ylims = (-.1,2)
        if (df['Infec_Div_Pop'].min()>=2) and (df['Infec_Div_Pop'].max()<=4):
            ylims = (1.9,4)

        plt.ylim(ylims[0],ylims[1])

       # print('Correlation: ',df.corr()['Total_Population']['Infection_Count'])
        return 

    wid_2 = widgets.Dropdown(
            options = infec_pop_merge['County'].unique().tolist(),
            description = 'County',
            disabled = False
    )

    interact(pop_v_infec_by_county, county = wid_2);
    

# year widget
def population_vs_infection_by_year():
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    plt.style.use('fivethirtyeight')
    import ipywidgets as widgets
    from ipywidgets import interact, interactive, fixed, interact_manual
    
    mrsa_merged = pd.read_csv('data/mrsa_merged.csv')
    infec_pop_merge = pd.read_csv('data/infec_pop_merge.csv')
    
    def pop_v_infec_by_year(year):    
    
        df = infec_pop_merge.loc[infec_pop_merge['Year'] == year]  
        df = df.drop(df['Total_Population'].idxmax())
        df['pop_by_100k'] = infec_pop_merge['Total_Population']/100000

        p = sns.lmplot(x='pop_by_100k',y='Infection_Count',data=df,ci=None,height=6,aspect=2)
        title = 'Infection Count Across Counties in Year '+ str(year)
        plt.title(title)
        plt.xlabel("Total Population Unit 100,000 People")
        plt.ylabel("Infection Count")
        plt.setp(p.ax.lines,linewidth=2)

        plt.ylim(-5,83)

        print('Slope of Regression Line: ',df.corr()['pop_by_100k']['Infection_Count'])
        return 
    
    wid_year = widgets.Dropdown(
            options = infec_pop_merge['Year'].unique().tolist(),
            description = 'Year',
            disabled = False
    )

    interact(pop_v_infec_by_year, year = wid_year);