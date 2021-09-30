import sqlite3
def db_connect():
    conn = sqlite3.connect('database.sqlite')
    return conn
def res_print(count):
    for row in count:
        print(row)

conn = db_connect()
cur = conn.cursor()
#cur.execute("SELECT * from Unique_Teams")
#print(cur.fetchall())
#cur.execute("SELECT * from Matches")
#print(cur.fetchall())
#cur.execute("SELECT * from Teams")
#print(cur.fetchall())
#cur.execute("SELECT * from Teams_in_Matches")
#print(cur.fetchall())
#cur.execute("PRAGMA table_info('Teams_in_Matches')")
#print(cur.fetchall())
#cur.execute("PRAGMA foreign_key_list('Unique_Teams')")
#print(cur.fetchall())
print("Home Team  and Away Team from matches where season is 2015 and FTHG is 5")
cur.execute("SELECT HomeTeam,AwayTeam from Matches where season =2015 and FTHG=5")
print(res_print(cur))

print("Matches where HomeTeam is 'Arsenal' and FTR is 'A'")
cur.execute("SELECT * from Matches where HomeTeam = 'Arsenal' and FTR = 'A'")
print(res_print(cur))

print("Matches where season is btw 2012 and 2015 and AwayTeam is 'Bayern Munich' and FTHG >2")
cur.execute("SELECT * from Matches where 2012 <= season <= 2015 and AwayTeam ='Bayern Munich' and FTHG >2")
print(res_print(cur))

print("Matches where HomeTeam starts with A and AwayTeam starts with M")
cur.execute("SELECT distinct * from Matches where HomeTeam LIKE 'A%' and AwayTeam LIKE 'M%'")
print(res_print(cur))

cur.execute("SELECT COUNT(*) from Teams")
print(f" Number of rows in Teams table is {cur.fetchall()[0][0]}")

cur.execute("SELECT distinct Season from Teams")
print(res_print(cur))

cur.execute("SELECT MAX(stadiumcapacity) from Teams")
print(f"Large:{cur.fetchall()[0][0]}")

cur.execute("SELECT MIN(stadiumcapacity) from Teams")
print(f"Small:{cur.fetchall()[0][0]}")

cur.execute("SELECT SUM(KaderHome) from Teams where season ='2014'")
sum1 = cur.fetchall()
print(f"Sum of squad players is : {sum1[0][0]}")

cur.execute("SELECT ROUND(AVG(FTHG),2) from Matches where HomeTeam='Man United'")
print(f"Average no: of goals:{cur.fetchall()[0][0]}")

print("Matches where season = 2010 and HomeTeam = 'Aachen'")
cur.execute("SELECT HomeTeam,FTHG,FTAG from Matches where season = 2010 and HomeTeam = 'Aachen' order by FTHG DESC,FTAG ASC ")
print(res_print(cur))

print("Total number of games won by each team in 2016")
cur.execute("SELECT HomeTeam,COUNT(FTR) from Matches where FTR ='H' and season = 2016 group by HomeTeam order by COUNT(FTR) DESC")
print(res_print(cur))

print("Ten rows from Unique Teams")
cur.execute("SELECT * from Unique_Teams LIMIT 10")
print(res_print(cur))

print("Printing the Match_ID and Unique_Team_ID with the corresponding Team_Name from the Unique_Teams and Teams_in_Matches tables")
cur.execute("SELECT  * from Unique_Teams JOIN Teams_in_Matches ON Teams_in_Matches.Unique_Team_ID = Unique_Teams.Unique_Team_ID LIMIT 10")
print(res_print(cur))

print("Joins together the Unique_Teams data table and the Teams table, and returns the first 10 rows.")
cur.execute("SELECT * from Unique_Teams JOIN Teams LIMIT 10")
print(res_print(cur))

print("shows the Unique_Team_ID and TeamName from the Unique_Teams table and AvgAgeHome, Season and ForeignPlayersHome from the Teams table. Only return the first five rows.")
cur.execute("SELECT Unique_Team_ID,Unique_Teams.TeamName,AvgAgeHome,Season,ForeignPlayersHome from Unique_Teams JOIN Teams ON Teams.TeamName = Unique_Teams.TeamName LIMIT 5")
print(res_print(cur))

print("Shows the highest Match_ID for each team that ends in a “y” or a “r”. Along with the maximum Match_ID, display the Unique_Team_ID from the Teams_in_Matches table and the TeamName from the Unique_Teams table.")
cur.execute("SELECT MAX(Match_ID), Teams_in_Matches.Unique_Team_ID,TeamName from Teams_in_Matches JOIN Unique_Teams ON Teams_in_Matches.Unique_Team_ID =Unique_Teams.Unique_Team_ID where (TeamName LIKE '%r') OR (TeamName LIKE '%a') group by Teams_in_Matches.Unique_Team_ID,TeamName")
print(res_print(cur))
conn.commit()
conn.close()
