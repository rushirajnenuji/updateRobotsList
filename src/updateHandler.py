


class updateHandler(object):
    """
        This class conatins the cunctionality to read and update the robots
        list based on the most recent COUNTER compliance files.
    """

    def __init__(self):
        pass

    def updateList(self):
        # Creating the file objects
        fullWebRobotList = open('../robots-list/fullWebRobotList.txt', 'r+')
        updatedCounterRobotsList = open('../robots-list/updatedCounterRobotsList.txt', 'r+')

        # Retreiveing the robots from both the files
        dataOneRobots = fullWebRobotList.readlines()
        counterRobots = updatedCounterRobotsList.readlines()

        print(len(dataOneRobots))
        print(len(counterRobots))
        count = 0

        # Updating the lists
        for i in counterRobots:
            if(i not in dataOneRobots):
                dataOneRobots.append(i)

        print(count)
        print(len(dataOneRobots))

        # Sort the list alphabetically
        dataOneRobots = sorted(dataOneRobots)

        print(len(dataOneRobots))

        # Setting the cursor at the beginning of the file
        fullWebRobotList.seek(0)

        # Over-write the fullWebRobotList.txt
        for i in dataOneRobots:
            fullWebRobotList.write(i)


        # Closing the file objects
        updatedCounterRobotsList.close()
        fullWebRobotList.close()


if __name__ == "__main__":
    handler = updateHandler()
    handler.updateList()
