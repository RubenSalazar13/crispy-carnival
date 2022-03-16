import json
import csv

def fun1(percent):
    #Remove percent sign
    percent = percent[:len(percent) - 1]
    #Change to float
    percentFloat = float(percent)
    #Divide by 100 to get value in decimal
    percentFloat /= 100
    #Return as string
    return f"{percentFloat:.2}"

def fun2(number):
    #Remove commas from the outputted number
    return number.replace(',', '')

def main():
    #Opening JSON file in read mode
    #Also, file path may need to be reverted to simple 'station-data.json'
    File = open('/home/ruben/Desktop/Python/IS4485-090/Mod8/station-data.json')
    Data = json.load(File)

    #Open a file for writing
    data_file = open('output.csv', 'w', newline='')
    #Create the csv writer object
    csv_writer = csv.writer(data_file)
    #Counter variable user for writing headers to the CSV file
    count = 0

    for data in Data:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1

    #Call fun1 and fun2
    for data in Data:
        if data['ValueType'].lower() == 'percent':
            data['Value'] = fun1(data['Value'])
        elif data['ValueType'].lower() == 'number':
            data['Value'] = fun2(data['Value'])
        csv_writer.writerow(data.values())
    data_file.close()

if __name__=='__main__':
    main()