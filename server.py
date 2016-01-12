from flask import Flask, render_template, request, redirect, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'my_secret_key'
mysql = MySQLConnector('nfl_teams')

@app.route('/')
def index():
    query = "select home_team.id, home_team.team_name as home, away_team.team_name as away_team, team_has_opponents.week from teams as home_team left join team_has_opponents on home_team.id = team_has_opponents.home_team_id left join teams as away_team on away_team.id = team_has_opponents.away_team_id"
    all_teams = mysql.fetch(query)
    return render_template('index.html',teams = all_teams)

#returns info on a single teams (as a partial or JSON)
@app.route("/teams/<int:id>", methods =["GET"])
def team_show(id):
    query = "SELECT * FROM teams WHERE id = {}".format(id)
    print query
    return "team_show"
#returns info on all teams (as a partial or JSON)
@app.route("/teams", methods =["GET"])
def team_index():
    query = "SELECT * FROM teams"
    teams = mysql.fetch(query)
    return render_template('teams_index.html', teams = teams);


#returns info on all players (as a partial or JSON)
@app.route("/players", methods =["GET"])
def player_index():
    query = "SELECT * FROM players"
    print query
    pass

if __name__ == '__main__':
  app.run(debug = True)
