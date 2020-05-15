import csv


def loadCSVData(filePath: str) -> list:
    """
    Loads a data from csv file

    ============= ===================================================================================
    **Arguments**
    filePath:     path of the csv file
    ============= ===================================================================================
    **Returns**
    A list of 3 element;
        1. A list of header names
        2. A list of 3 lists, each list contain the data of a single column
        3. A list of tuples contains the data of each row.
    ============= ===================================================================================
    """
    with open(filePath) as csvFile:
        csv_reader = csv.reader(csvFile)
        headers = []
        dataTuple = []
        dataList = [[], [], []]

        # Get the header names
        for row in csv_reader:
            for col in range(len(row)):
                headers.append(row[col])
            break

        # Get the list of each column
        for row in csv_reader:
            for i in range(len(row)):
                dataList[i].append(row[i])

        # Get the list of tuples for each row
        for i in range(len(dataList[0])):
            dataTuple.append((dataList[0][i], dataList[1][i], dataList[2][i]))

    return [headers, dataList, dataTuple]



if __name__ == '__main__':
    headers, dataLists, dataTuples = loadCSVData('Data.csv')
    print(headers)
    print(dataLists)
    print(dataTuples)
