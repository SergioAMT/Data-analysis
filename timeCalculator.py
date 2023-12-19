import math

def add_time (startTime, duration, dayOfWeek = False):
    startHour = startTime.split(':')[0]
    startMinute = startTime.split(':')[1][0:2]
    amOrPm = startTime.split(':')[1][3::]
    durationHour = duration.split(':')[0]
    durationMinute = duration.split(':')[1][0:2]
    minutes = 0
    minutesFinal = 0
    am_and_pm_flip = {'AM':'PM','PM':'AM'}
    daysOfTheWeekIndex  = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
    daysOfTheWeekArray = ['Monday', 'Tuesday', 'Wednesday', 'Thurday', 'Friday', 'Saturday', 'Sunday']
    amounOfDays = int(durationHour) / 24
    newDay = ''
    index = 0
    
    totalHour = (int(startHour) + int(durationHour))
    totalMinutes = (int(startMinute) + int(durationMinute))
    div = math.floor(totalHour / 12)
    finalHour = totalHour - (12 * div)
    
    if totalMinutes >= 60:
        minutes = totalMinutes / 60
        finalHour = math.floor(finalHour + minutes)
        minutesFinal = '0'+str(totalMinutes - 60)
    else:
        minutesFinal = totalMinutes
        
    amount_am_and_pm_flip = int(startHour) + int(durationHour) % 12
    
    if finalHour < 10:
        finalHour1 = '0'+ str(finalHour)
    else:
        finalHour1 = str(finalHour)
    
    amOrPm = am_and_pm_flip[amOrPm] if amount_am_and_pm_flip % 2 == 1 else amOrPm
    
    returnTime = str(finalHour1) + ':' + str(minutesFinal) + '' + amOrPm
    # print(finalHour1,':', minutesFinal, amOrPm)
    
    if(dayOfWeek):
        dayOfWeek = dayOfWeek.lower()
        index = int((daysOfTheWeekIndex[dayOfWeek]) + amounOfDays) % 7
        newDay = daysOfTheWeekArray[index]
        returnTime += ', ' + newDay
        
        if(amounOfDays == 1):
            return returnTime + '' + '(next day)'
        elif(amounOfDays > 1):
            return returnTime + ' (' + str(amounOfDays) + 'days later)'
            
    return returnTime
    
    
add_time('11:23 AM', "13:20", 'Friday')
    
    