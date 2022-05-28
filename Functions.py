# reading the file
import pandas as pd
main_data = pd.read_csv("Data.csv")

# cleaning the data
# making the values of the as float from intger.  
main_data["ARAI_Certified_Mileage_kmpl"].astype(float)
# removing the duplicates based on the rows
main_data = main_data.drop_duplicates(subset="Model")
# for now top cars = data.head
top_cars =main_data[main_data['Model'].isin(["Scorpio", "Thar", "Xuv500", "Fortuner","Vitara Brezza"])]
# average top cars 


def cars(cost_min, cost_max, brand, mileage_min, mileage_max, p_d_cng, seating, data=main_data):
    #validating the inputs
    try:
        cost_min = int(cost_min)
    except:
        return "You have entered invalid minimum cost, please re-enter"
    try:
        cost_max = int(cost_max)
    except:
        return "You have entered invalid maximum cost, please re-enter"
    try:
        mileage_min = int(mileage_min)
    except:
        return "You have entered invalid mimum mileage, please re-enter"
    try:
        mileage_max = int(mileage_max)
    except:
        return "you have entered invalid max mileage, please re-enter"

    
    # now giving results
    filter_p = data[data["Ex-Showroom_Price"].isin(range(min(cost_min,cost_max), max(cost_min,cost_max)))]
    if (len(filter_p) == 0):
        return "none"

    filter_b_p = filter_p[filter_p["Make"] == brand]
    if (len(filter_b_p) == 0):
        return filter_p.sort_values("Ex-Showroom_Price").head()

    filter_b_p_t = filter_b_p[filter_b_p["Fuel_Type"]  == p_d_cng]
    if (len(filter_b_p_t) == 0):
        return filter_b_p.sort_values("Ex-Showroom_Price").head()

    filter_b_m_p_t = filter_b_p_t[filter_b_p_t["ARAI_Certified_Mileage_kmpl"].isin(range(min(mileage_min, mileage_max), max(mileage_min, mileage_max)))]
    if (len(filter_b_m_p_t) == 0):
        return filter_b_p_t.sort_values("Ex-Showroom_Price").head()

    filter_b_m_p_s_t = filter_b_m_p_t[filter_b_m_p_t["Seating_Capacity"] == seating]
    if (len(filter_b_m_p_s_t) == 0):
        return filter_b_m_p_t.sort_values("Ex-Showroom_Price").head()





# def car_found_desc(data):
    # this fuction will take the output 5 rows data frame to generate a text description of it
    # input: 5 row pandas dataframw
    # output: an array of len 5, where ith index will contain description of ith car, in around 70 words

