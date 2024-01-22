import julian
import datetime
from PyAstronomy import pyasl
#ADİLHAN KOÇAK
#this function adds leap seconds to the utc values we entered and converts them to TAI and GPST dates
#İNPUT = UTC[1X4]
#OUTPUT = TAI[1X4],GPST[1X4],TT[1X4]


#create function of convert time 
def convertime(utc):
    
    #I found the leap second values format of modify julian date
    LeapSecondYearMJulian = [41499,41683,42048,42413,42778
                         ,43144,43509,43874,44239,44786,45151
                         ,45516,46247,47161,47892,48257,48804
                         ,49169,49534,50083,50630,51179,53736
                         ,54832,56109,57204,57754]
    
    #3rd input format of hour because of the datetime function so we should write hour format in 3rd.
    #UTC TO MODİFY JULİAN DATE
    
    df = datetime.datetime(utc[0],utc[1],utc[2],utc[3])
    mjul = pyasl.jdcnv(df) - 2400000.5
    
    #I CHECK THE NUMBER OF LEAP SECOND SİNCE HAVE BEEN FOR THE DF
    cls = 0
    for i in LeapSecondYearMJulian:

        if mjul >= i:
            cls +=1
 
#I added leap second in modify julian date and convert UTC 
    UTC = julian.from_jd(mjul, fmt='mjd')

#I ADDED LEAP SECONDS THİS PART BECAUSE OF THE DATETİME FUNCTİON

    #UTC TO TAI
    
    UTC_TAI = UTC + datetime.timedelta(0,10+cls)
    TAI = UTC_TAI
    print(f"UTC : {[UTC.year,UTC.month,UTC.day,UTC.hour*3600+UTC.minute*60+UTC.second+UTC.microsecond/1000000]}  TAI : {[TAI.year,TAI.month,TAI.day,TAI.hour*3600+TAI.second+TAI.microsecond/1000000]}")
    
    #UTC TO GPST
    #if utc[0] <= 1989:
        #print("Year must be greater than 1980 For GPST clock")
    #else:
        
    UTC_GPST = UTC + datetime.timedelta(0,cls-9)
    GPST = UTC_GPST
    print(f"UTC : {[UTC.year,UTC.month,UTC.day,UTC.hour*3600+UTC.minute*60+UTC.second+UTC.microsecond/1000000]}  GPST : {[GPST.year,GPST.month,GPST.day,GPST.hour*3600+GPST.minute*60+GPST.second+GPST.microsecond/1000000]}")
        
    #TAI TO TT
    TAI_TT = TAI + datetime.timedelta(0,32.184)
    TT = TAI_TT
    print(f"TAI : {[TAI.year,TAI.month,TAI.day,TAI.hour*3600+TAI.second+TAI.microsecond/1000000]}  TT : {[TT.year,TT.month,TT.day,TT.hour*3600+TT.minute*60+TT.second+TT.microsecond/1000000]}")

convertime([1972,7,1,1])
