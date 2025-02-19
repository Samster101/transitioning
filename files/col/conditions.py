from orderlist_part2 import stock_sheet_entry
import math
products = {
    "Nutella":          {"Amount": 2, "Cost": 63.99, "script_code" : "A","script_code_arguement" : 0.6},
    "Caramel":          {"Amount": 12, "Cost": 55.69, "script_code" : "B","script_code_arguement" : 0.5 },
    "Chocolate Chips":  {"Amount": 25, "Cost": 107.25, "script_code" : "B","script_code_arguement" : 0.5},
    "Coconut Flakes":   {"Amount": 10, "Cost": 37.79, "script_code" : "A","script_code_arguement" : 0.5},
    "Granola":          {"Amount": 1, "Cost": 120.49, "script_code" : "A","script_code_arguement" : 0.6},
    "Almond Milk" :     {"Amount" : 12, "Script_code" : "A","script_code_arguement" : 0.6 },
    "Aluminum Water Bottles": {"Amount": 24, "Cost": 28.59, "script_code" : "B","script_code_arguement" : 0.5},
    "Dragon Fruit Cubes": {"Amount": 8, "Cost": 28.69},"script_code" : "B","script_code_arguement" : 0.5,
    "Baby Kale":        {"Amount": 2, "Cost": 19.79,"script_code" : "B","script_code_arguement" : 0.5},
    "Acerola Packs":    {"Amount": 24, "Cost": 29.55,"script_code" : "B","script_code_arguement" : 0.5},
    "White Chocolate" : {"script_code" : "C" },
    "Almond Milk" : {"script_code" : "C" },
    "Pineapple Juice" : {"script_code" : "C" }
}
Cheney_list = ["Nutella","Caramel","Chocolate Chips","Coconut Flakes","Aluminum Water Bottles"]
Cheney_Only = ["Almond Milk","Pineapple Juice","White Chocolate"]



####SCRIPT CODES----->
"Some items are split like 70% quanitity day 1 and 30% next time, or given in day 1 fully if amount under a percentage. "
"Code A: product item key requires an additional key for percentage amount, make this a list for expandability"
"Code B requires a percetnage key, idk how if needed expandability"

####list with element conditions

##THIS FUNCTION SPLITS THE ORIGINAL LIST WITH ITEMS THAT CAN ONLY BE ORDERED VIA CHENEY! CODE C****
def _cheney_only(stock_sheet_entry,cheney_list):
    cheney_only_order_list = []
    for items in stock_sheet_entry:
        if items[0] in cheney_list:
            try: 
                if products[items[0]]["script_code"] != "C":  
                    amount = -_O_amount_conv(items,products)
                    cheney_only_order_list.append([items[0],amount])
                else:
                    cheney_only_order_list.append([items[0],1])
            except: pass
    return cheney_only_order_list


#operator to convert stock sheet amounts to order amounts
def _O_amount_conv(counted_amounts,set_quantity):
    if counted_amounts[2] < counted_amounts[1]:
        try:
            order_amount = math.ceil((counted_amounts[1] - counted_amounts[2]) / set_quantity[counted_amounts[0]]["Amount"])
        except: pass
        return [counted_amounts[0],0,order_amount]


##NEED TO SETUP-> returns true if acai day 1 > day 2
def condition_acai():
    return False


    
#Condition -- less than percentage, add to day one. CODE B*********
def less_than_condition(a,b):
    if float(a[2]/a[1]) <= b:
        return True


#expandable by making this function acept akwargs or a list, and then systematically 
#progess thru that list. CODE A *******
def split_items(a,b):
    arb_1 = math.ceil(a*b)
    arb_2 = math.floor(a*(1-b))
    return [arb_1,arb_2]
    pass


def delete_elements(list_1,list_2):
    for arb_i , arb_x in enumerate(list_2):
        for arb_z in list_1:
            if arb_z[0] == arb_x[0]:
                list_2.pop(arb_i)
    return list_2


###
##CREATE 2 list for days order, example lincolnton has 2 order days so this has 2 lists, to create expandable make list that works with n. l1 is tuesday and l2 is satudrday.
def dist_and_collect(a):
    l1 = []
    l2 = []
    for i in a:
        try:
            if products[i[0]]["script_code"] != "C":
                order_ = _O_amount_conv(i,products)

            if products[i[0]]["script_code"] == "A":
                arb_l = split_items(order_[2],products[i[0]]["script_code_arguement"])
                l1.append([i[0],arb_l[0]])
                l2.append([i[0],arb_l[1]])

            if products[i[0]]["script_code"] == "B":
                if less_than_condition(i,0.5):
                    l1.append(l1.append([i[0],order_[2]]))
                else: 
                    l2.append([i[0],order_[2]])
        except: pass
        l1 = [i for i in l1 if i != None]
        l2 = [i for i in l2 if i != None]
    return [l1,l2]



def if_acai_condition(l,ch):
    arb_bool = True
    arb_list_ = []
    if condition_acai():
        arb_list = l[0]
        arb2_list = l[1]
        arb_bool = False
    else: 
        arb_list = l[1]
        arb2_list = l[0]

    for arb_i,arb_y in enumerate(arb_list):
        if arb_y[0] in ch:
            arb_l = [i for i in arb_y]
            arb_list_.append(arb_l)
            arb_list.pop(arb_i)
    ## PACKAGE DATA INTO DATA PACKAGE
    ###
    ###
    #print(arb_l)
    if arb_bool:
        d_1_sysco = arb2_list
        d_2_syco = arb_list
        d2_cheney = arb_list_
        data_package = [d_1_sysco,d_2_syco,d2_cheney,"D2"]
    else:
        d_1_sysco = arb_list
        d_2_syco = arb2_list
        d1_cheney = arb_list_
        data_package = [d_1_sysco,d_2_syco,d1_cheney,"D1"]
    return data_package

        


#starts the iteration
def startfuntion():
    #get stock sheet
    quantity = stock_sheet_entry()
    lc = _cheney_only(quantity,Cheney_Only)
    new_quantity = delete_elements(lc,quantity)
    arb_list = if_acai_condition(dist_and_collect(new_quantity),Cheney_list)
    o_d_1_s = arb_list[0]
    o_d_2_s = arb_list[1]
    if arb_list[-1] == "D1":
        #grab orders
        o_c = [arb_list[2],"D1"]
    else:
        o_c = [arb_list[2], "D2"]
    
    print(o_d_1_s,"\n\n",o_d_2_s,"\n\n",o_c)
    

    




startfuntion()
            
    



    


#Nutella = 23