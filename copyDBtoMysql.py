import pandas as pd
import mysql.connector

# 3 - full name, 4 - position, 5 - rating, 7 - worth, 8 - wage, 10 - date of birth, 11 - height, 12 - weight
# 14 - team name, 15 - league name, 18 - shirt number, 23 - nationality
# rating?

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="qawZSE123",
  database="fifa"
)
mycursor = mydb.cursor()

def install_data_inDB(path):
    columns_to_extract = [3, 4, 5, 7, 8, 10, 11, 12, 14, 15, 18, 23]
    player_query = "INSERT INTO player (full_name, date_of_birth, nationality) VALUES (%s, %s, %s)"
    team_query = "INSERT INTO team (name, league_id) VALUES (%s, %s)"
    employ_query = "INSERT INTO employ (player_id, team_id, year," \
                   " position, rating, height, weight, worth, wage, jersey_number)" \
                   " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    league_query = "INSERT INTO league (name, country) VALUES (%s, %s)"
    chunk_size = 1000
    team_list = {}
    league_list = {}
    for chunk in pd.read_csv(path, usecols=columns_to_extract, chunksize=chunk_size):
        # Process each chunk and insert data into MySQL

        for index, row in chunk.iterrows():
            if any(pd.isnull(row)):
                continue
            mycursor.execute(player_query, (row[0], row[5], row[11]))
            player_id = mycursor.lastrowid

            # country missing
            if row[9] not in league_list.keys():
                mycursor.execute(league_query, (row[9], 'Nauru'))
                league_id = mycursor.lastrowid
                league_list[row[9]] = league_id
            else:
                league_id = league_list[row[9]]

            if row[8] not in team_list.keys():
                mycursor.execute(team_query, (row[8], league_id))
                team_id = mycursor.lastrowid
                team_list[row[8]] = team_id
            else:
                team_id = team_list[row[8]]

            mycursor.execute(employ_query, (player_id, team_id, 2022, row[1], row[2], row[6],
                                            row[7], row[3], row[4], row[10]))

    mydb.commit()


if __name__ == '__main__':
    install_data_inDB(r'C:\Users\artte\Downloads\archive\players_22.csv')
    mycursor.close()

