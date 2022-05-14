#calender
# enter date (1/1/2017) to know the day
#enter month (1/2017) to know days
# higri history

import math
def ex(a):
       if a.count('/') == 1 :
              dy = 0
              mth =  int(a[:a.index('/')])
              yr = int(a[a.index('/')+1:])
       else :
              dy = int(a[:a.index('/')])
              mth = int(a[a.index('/')+1:a.index('/',a.index('/')+1)])
              yr = int(a[a.index('/',a.index('/')+1)+1:])
       if (yr%4) == 0:
              fb = 29 ; yr_n = 366
       else:
              fb = 28 ; yr_n = 365 
       return dy,mth,yr,fb,yr_n

##################################################################
def pre_birth(year):  # this function to know the first day in the year for past
    global first 
    if year == 0 :
        print('this year not exist')
        return 
    if year < 0:
        year += 1
    d = ['sun','sat','fri','thu','wed','tus','mon']
    y = 2017
    n = 0
    while y >= year :
        first =d[n]
        y -= 1
        if y % 4 == 0:
            n += 2
        else:
             n += 1
        if n > 6 :
                n = n - 7
    return first
###################################################################
def suf_birth(year):  # this function to know the first day in the year for future
    global first 
    d = ['sun','mon','tus','wed','thu','fri','sat']
    y = 2017
    n = 0
    while y <= year :
        first =d[n]
        y += 1
        if y % 4 == 0:
            n += 2
        else:
             n += 1
        if n > 6 :
                n = n - 7
    return first
###################################################################
def list_days(num_d_year , first_day ):
       lis = ['sat','sun','mon','tus','wed','thu','fri']
       ind = lis.index(first_day)  
       arranged_list = lis[ind:]+lis[:ind]  # to rearrange the list of days
       days_list = []
       year_days = 1 ; n = 0
       while year_days <= num_d_year :   # this loop to create list with year days
           days_list.append(arranged_list[n])   
           n+=1
           if n == 7:
               n=0
           year_days+=1
       return days_list
#######################################################
def print_year(feb , first_day,mon):
        m=1
        lis =['sat','sun','mon','tus','wed','thu','fri']
        li=lis.index(first_day)

        while m<13:
            if m in [1,3,5,7,8,10,12]:
                d =31
            elif m in [4,6,9,11]:
                d = 30
            elif m == 2 :
                d = feb
            w = 1
            if m == mon :
                   print('  sat    sun     mon   tus     wed     thu     fri')
            i=0
            first_space =''
            while i<li:
                first_space += '           '
                i+=1
            if m == mon :   
                   print(first_space,end='')    
            while w < d+1:
                if w in range(0,10):
                    space='  '
                elif w in range(10,32):
                    space=''
                if m == mon :
                       print(space,w,end='      ')
                li+=1
                w += 1
                if li == 7:
                    li=0
                    if m == mon :
                           print('')
            if m == mon :              
                   print('')
            m+=1
######################################################
##ses =  المناسبات والاحداث
###################################################################
def higri(days,year):
       total = math.fabs((263 + 2017 * 365.25) -  (days + (year * 365.25)))
       num_higri = total / 354
       #print(total,'.....',num_higri)
       if (days + (year * 365.25)) < (263 + 2017 * 365.25) :
              if num_higri >  int(num_higri) :
                     result = 1438 - (int(num_higri))
              else :
                     result = 1438 - num_higri
       elif (days + (year * 365.25)) > (263 + 2017 * 365.25) :
              if num_higri >  int(num_higri) :
                     result = 1438 + (int(num_higri) + 1)
              else :
                     result = 1438 + num_higri
       else:
              result = 1438
       return result
######################################################

while True :
       first = ''
       hist = input('enter history (2/4/2005) q for quit: ')
       if hist == 'q':
              break
       try :
              if hist.count('/') == 1 :
                     cc = ex(hist)
                     if cc[2] <= 2017:  # know the first day in the year
                            pre_birth(cc[2])
                     else:
                            suf_birth(cc[2])
                     print_year(cc[3],first,cc[1])
              else:
                     cc = ex(hist)  # get day,month,year and num of february and year days
                     num = [31,cc[3],31,30,31,30,31,31,30,31,30,31]
                     request = sum(num[0:cc[1]-1])+cc[0]   # know the number of the day in the year
                     if cc[2] <= 2017:  # know the first day in the year
                            pre_birth(cc[2])
                     else:
                            suf_birth(cc[2])
                            
                     dl = list_days(cc[4] , first ) # create list with year days
                     print(dl[request-1]) # print request day
                     ##########################
                     h = higri(request , cc[2])
                     print(h, ' higri')
                     # list of events
                     # print(yl[cc[1]-1][cc[0]-1]
       except :
              print('retry')
