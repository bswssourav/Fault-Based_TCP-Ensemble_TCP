""" 

    This is the main python file which initiates the program.

"""

import sys
import Utils.rankGen as GenRank
import Utils.readFile as ReadFile
from configparser import ConfigParser
from py3votecore.schulze_pr import SchulzePR

if __name__=="__main__":
    config_object = ConfigParser()
    config_object.read('config.ini')
    FilePath = config_object["PATHS"]['InputFilePath']
    print("Reading Fault matrix from file at : ",FilePath)
    formattedLinesList = ReadFile.ReadAndFormatFile()
    # print(formattedLinesList)
    rank1 = list(map(lambda el:[str(el)], formattedLinesList[1]))
    rank2 = list(map(lambda el:[str(el)], formattedLinesList[2]))
    print(rank1,rank2)
    input = [
                {"count": 1, "ballot": rank1},
                {"count": 1, "ballot": rank2}
            ]
    output = SchulzePR(input, ballot_notation=SchulzePR.BALLOT_NOTATION_GROUPING).as_dict()

    print(output["order"])
    # rankList = GenRank.generate(formattedLinesList)[0] # contains final Rank List
    # print("\n\n______________________________________________\n\n")
    # print("The Ranking of " + str(len(rankList)) + " Test Cases is as follows:\n")
    # for i in range (len(rankList)):
    #     print("Rank", (i+1),"-> Test Case",rankList[i])
    # print("\n______________________________________________\n\n")
    # print (" ".join(map(str,rankList)))

    
