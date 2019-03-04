<?php
// This file contains the configurations for server connection. Located on server.
require('/var/.config.php');

// Display the header
echo nl2br("Name: Brice Allard \n Assignment: A04 - Nfl Stats \n Date: 02/28/2019 \n\n");
echo "================================================================";

// Connect to dataabase
$mysqli = mysqli_connect($host, $user, $password, $database);

// If connection fails
if (mysqli_connect_errno($mysqli)) {
    echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

function f(){
    ob_flush();
    flush();
}

/**
 * Pulls a player out of players table and returns:
 *     [name] => Player.Name
 * Params:
 *     playerId [string] : id of type => 00-000001234
 * Returns:
 *     name [string] : => T. Smith
 */
function getPlayer($playerId){
    global $mysqli;
    $sql = "SELECT `name` FROM players WHERE id = '{$playerId}' LIMIT 1";
    $response = runQuery($mysqli,$sql); 
    if(!array_key_exists('error',$response)){
        return $response['result'][0]['name'];
    }
    return null;
}

/**
 * Prints a question plus a border underneath
 * Params:
 *     question [string] : "Who ran the most yards in 2009?"
 *     pads [array] : [3,15,15,5] padding for each data field
 * Returns:
 *     header [string] : Question with border below
 */
function printHeader($question,$pads,$cols){
    if(strlen($question) > array_sum($pads)){
        $padding = strlen($question);
    }else{
        $padding = array_sum($pads);
    }
    $header = "\n<b>";
    $header .= "{$question}\n\n";
    for($i=0;$i<sizeof($cols);$i++){
        $header .= str_pad($cols[$i],$pads[$i]);
    }
    $header .= "\n".str_repeat("=",$padding);
    $header .= "</b>\n";
    return $header;
}

/**
 * formatRows:
 *    Prints each row with a specified padding for allignment
 * Params:
 *    $row [array] - array of multityped values to be printed
 *    $cols [array] - array of ints corresponding to each column size wanted
 * Example:
 *    
 *    $row = ['1','00-00000123','T. Smith','329']
 *    $pads = [4,14,20,5]
 */
function formatRows($row,$pads){
    $ouput = "";
    for($i=0;$i<sizeof($row);$i++){
        $output .= str_pad($row[$i],$pads[$i]);
    }
    return $output."\n";
}

/**
 * displayQuery: print question + sql result in a consistent and 
 *               formatted manner
 * Params: 
 *     question [string] : question text
 *     sql [string] : sql query
 *     cols [array] : column headers in array form
 *     pads [array] : padding size in ints for each column
 */
function displayQuery($question,$sql,$cols,$pads){
    global $mysqli;
    $parts = explode('.',$question);
    if($parts[0]%2==0){
        $color="#C0C0C0";
    }else{
        $color = "";
    }
    echo"<pre style='background-color:{$color}'>";
    echo printHeader($question,$pads,$cols);
    $response = runQuery($mysqli,$sql);
    if($response['success']){
        foreach($response['result'] as $id => $row){
            $id++;
            $row['id'] = $id;
            $row['name'] = getPlayer($row['playerid']);
            $row[0] = $row[$cols[0]];
            $row[1] = $row[$cols[1]];
            $row[2] = $row[$cols[2]];
            $row[3] = $row[$cols[3]];
            $row[4] = $row[$cols[4]];
            echo formatRows($row,$pads);
        }
    }
    echo"</pre>";
    f();
}

/**
 * This function runs a SQL query and returns the data in an associative array
 * that looks like:
 * $response [
 *      "success" => true or false
 *      "error" => contains error if success == false
 *      "result" => associative array of the result
 * ]
 */
function runQuery($mysqli,$sql){
    $response = [];

    // run the query
    $result = $mysqli->query($sql);

    // If we were successful
    if($result){
        $response['success'] = true;
        
        while($row = $result->fetch_assoc()){
            $response['result'][] = $row;
        }
        $result->free();
    }else{
        $response['success'] = false;
        $response['error'] = $mysqli->error;
    }

    return $response;
}

/**
 * 
 * ALL QUESTIONS FOR ASSIGNMENT BELOW
 * 
 */
echo"</pre>";

/**
 * Question 1
 */
$question = "1. Count number of teams an individual player played for.";
$pads = [5,20,12,5];
$sql = "SELECT id as playerid,name,count(distinct(club)) as count 
        FROM `players` 
        GROUP BY id,name 
        ORDER BY `count` 
        DESC LIMIT 5";
$response = runQuery($mysqli,$sql);
$cols = ['id','name','count'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 2
 */
$question = "2. Find the players with the highest total rushing yards by year, and limit the result to top 5.";
$pads = [3,12,20,8,8];
$sql = "SELECT playerid, season, sum(yards) as tot_yards 
        FROM `players_stats` 
        WHERE statid=10 or statid=75 or statid=76 
        GROUP BY season, playerid 
        ORDER BY tot_yards 
        DESC LIMIT 5";
$response = runQuery($mysqli,$sql);
$cols = ['id','playerid','name','season','tot_yards'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 3
 */
$question = "3. Find the bottom 5 passing players per year.";
$pads = [3,12,20,8,8];
$sql = "SELECT playerid, season, sum(yards) as tot_yards 
        FROM `players_stats` 
        WHERE statid=15 or statid=16 or statid=77 
        GROUP BY season, playerid
        ORDER BY tot_yards 
        ASC LIMIT 5";
$cols = ['id','playerid','name','season','tot_yards'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 4
 */
$question = "4. Find the top 5 players that had the most rushes for a loss.";
$pads = [3,12,20,8,8];
$sql = "SELECT playerid, season, count(yards) as tot_yards
        FROM `players_stats` 
        WHERE yards < 0 and statid=10
        GROUP BY season, playerid
        ORDER BY tot_yards
        DESC LIMIT 5";
$cols = ['id','playerid','name','season','tot_yards'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 5
 */
$question = "5. Find the top 5 teams with the most penalties.";
$pads = [3,8,10];
$sql = "SELECT club, sum(pen) as tot_penalties
        FROM `game_totals`
        GROUP BY club
        ORDER BY tot_penalties
        DESC LIMIT 5";
$cols = ['id','club','tot_penalties'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 6
 */
$question = "6. Find the average number of penalties per year.";
$pads = [3,8,16,10];
$sql = "SELECT season, sum(pen) as tot_penalties, count(gameid) as tot_games, sum(pen) / count(gameid) as avg_penalties
        FROM `game_totals`
        GROUP BY season";
$cols = ['id','season','tot_penalties','avg_penalties'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 7
 */
$question = "7. Find the Team(s) with the least amount of average plays every year.";
$pads = [5,8,8,10];
$sql = "SELECT gamesperclub.season as season ,gamesperclub.club as club, count(Distinct playid)/gamesperclub.count as avgplays 
        FROM plays,
            (SELECT club,  count(DISTINCT gameid) as count, season 
            FROM `game_totals` group by season, club) as gamesperclub 
        WHERE gamesperclub.club=plays.clubid 
        GROUP BY gamesperclub.season,gamesperclub.club 
        ORDER BY season,avgplays 
        ASC";
$cols = ['id','season','club','avgplays'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 8
 */
$question = "8. Find the top 5 players that had field goals over 40 yards.";
$pads = [3,12,20,10,10];
$sql = "SELECT playerid, yards, sum(yards) as tot_yards, count(playid=70) as tot_count
        FROM `players_stats`
        WHERE yards > 40 and statid=70
        GROUP BY playerid
        ORDER BY tot_count
        DESC LIMIT 5";
$cols = ['id','playerid','name','tot_yards','tot_count'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 9
 */
$question = "9. Find the top 5 players with the shortest avg field goal length.";
$pads = [3,12,20,10];
$sql = "SELECT playerid, avg(yards) as avg_yards
        FROM `players_stats`
        WHERE statid=70
        GROUP BY playerid
        ORDER BY avg_yards
        ASC LIMIT 5";
$cols = ['id','playerid','name','avg_yards'];
displayQuery($question,$sql,$cols,$pads);

/**
 * Question 10
 */
$question = "10. Rank the NFL by win loss percentage (worst first).";
$pads = [3,6,8];
$sql = "SELECT `club`, sum(if(`wonloss` like 'won',1,0))/ sum(if(`wonloss` like 'loss',1,0)) as winlossration 
        FROM `game_totals` 
        GROUP BY club 
        ORDER BY winlossration 
        ASC LIMIT 10";
$cols = ['id','club','winlossration'];
displayQuery($question,$sql,$cols,$pads);

// /**
//  * Question 11
//  */
// $question = "11. Find the top 5 most common last names in the NFL.";
// $pads = [3,5];
// $sql = "SELECT AVG(count) as average_plays
// FROM (
//     SELECT count(distinct(playid)) as count FROM `players_stats` group by gameid
// ) as count";
// $cols = ['id','average_plays'];
// displayQuery($question,$sql,$cols,$pads);