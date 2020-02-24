# line graph widget
def infection_rates_per_county():
    !pip install ipywidgets 
    # %matplotlib inline
    from ipywidgets import interact, interactive, fixed, interact_manual
    def line_county(County):
        plt.figure(figsize=(10,5));
        x = list(mrsa_merged.loc[mrsa_merged['County']== County].groupby(['Year']).agg(sum).index)
        y = list(mrsa_merged.loc[mrsa_merged['County']== County].groupby(['Year']).agg(sum)['Infection_Count'])
        sns.lineplot(x,y)
        plt.xlabel("Year")
        plt.ylabel("County");
        return 

    wid_1 = widgets.Dropdown(
            options = mrsa_merged['County'].unique().tolist(),
            description = 'County',
            disabled = False
    )

    interact(line_county, County = wid_1);


# scatter plot widget - population versus infection rate per county by year
def population_vs_infection_by_county():
    pip install ipywidgets 
    # %matplotlib inline
    from ipywidgets import interact, interactive, fixed, interact_manual   
    
    def pop_v_infec_by_county(county):    
        
        df = infec_pop_merge.loc[infec_pop_merge['County'] == county]  
        p = sns.lmplot(x='Total_Population',y='Infection_Count',data=df,ci=None,aspect=2)
        plt.title('Population Versus Infection Rate Per County Across Years')
        plt.xlabel("Total Population by Year")
        plt.ylabel("Infection Rate")
        plt.setp(p.ax.lines,linewidth=2)
        return 

    wid_2 = widgets.Dropdown(
            options = infec_pop_merge['County'].unique().tolist(),
            description = 'County',
            disabled = False
    )

    interact(pop_v_infec_by_county, county = wid_2);


# scatter plot widget - population versus infection rate by year
def population_vs_infection_by_year():
    pip install ipywidgets 
    # %matplotlib inline
    from ipywidgets import interact, interactive, fixed, interact_manual
    
    def pop_v_infec_by_year(year):    
        
        df = infec_pop_merge.loc[infec_pop_merge['Year'] == year]  
        p = sns.lmplot(x='Total_Population',y='Infection_Count',data=df,ci=None,aspect=2)
        plt.title('Population Versus Infection Rate Across Counties Over the Year')
        plt.xlabel("Total Population")
        plt.ylabel("Infection Rate ")
        plt.setp(p.ax.lines,linewidth=2)
        return 

    wid_3 = widgets.Dropdown(
            options = infec_pop_merge['Year'].unique().tolist(),
            description = 'Year',
            disabled = False
    )

    interact(pop_v_infec_by_year, year = wid_3);