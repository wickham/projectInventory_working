'''
    This program is for open source use
    Designed by Allen Wickham
    Q3 2017
    Project info @
    www.allenwickham.me
    Contact:
    allenwickhamiii@gmail.com
'''

def html(): 
    html = """\

    <!DOCTYPE html>

    <html>
                <head>
                <style>
                html,body{
                    overflow-x: hidden;
                }

                table {
                    font-family: arial, sans-serif;
                    border-collapse: collapse;
                    width: 100%;
                }

                h1 {
                    font-family: helvetica, arial, sans-serif;
                    color: white;
                }

                h2 {
                    font-family: helvetica, arial, sans-serif;
                    color: black;
                    
                }

                td, th {
                    border: 1px solid #dddddd;
                    text-align: left;
                    padding: 8px;

                }

                td.good, td.received {
                    background-color: rgba(156,225,89, 0.7);
                }
                
                td.out, td.need {
                    background-color: rgba(255,95,94, 0.7);
                }
                
                td.low, td.order {
                    background-color: rgba(255,254,97, 0.7);
                }
                
                th.dark, tr.dark{
                    background-color: rgb(40,40,40);
                    border-bottom: 1px solid black;
                    color: rgb(255,255,255);

                }

                th.red, tr.red{
                    background-color: rgb(40,40,40);
                    border-bottom: 1px solid black;
                    color: rgb(255,255,255);

                }
                
                tr {
                    background-color: rgb(255,255,255);
                }

                tr:nth-child(even) {
                    background-color: #dddddd;
                }

                tr.bro {
                    
                    background-color: rgb(255,150,150);
                }

                tr.bro:nth-child(even) {
                    background-color: rgb(255,190,150);
                }

                div.head {
                    background: rgba(255,255,255,.6);
                }

                div.good {
                    background: linear-gradient(to top right,rgba(100,178,223,.8),rgba(36,66,142,.7)); 
                    padding:25px;
                    margin: 20px 10px 10px 10px; 
                    text-align: right;
                    border-radius: 25px;
                    box-shadow: -5px 5px 4px #aaa,
                                 5px 4px 4px #aaa;
                    min-width: 320px;

                }
                
                div.bad {
                    background-color:rgb(255,190,190); 
                    border: 1px solid rgb(255,150,150);
                    padding-top: 1px;
                    padding-bottom: 25px; 
                    margin-top: 20px;
                    margin: 20px 0px 0px 0px; 
                    border-radius: 25px;

                }
                .fixed {
                    min-width: 5em;
                }

                .special { 
                    font-family: "Baskerville Old Face",Dingbats, Quivira, "Arial Unicode MS", Symbola, " Everson Mono";
                    font-size: 50px;
                    color: white;
                    text-overflow: clip;
                    overflow: hidden;
                    width: 4em;    
                }

                .special1 { 
                    font-family: "Dingbats", Quivira, "Arial Unicode MS", Symbola, " Everson Mono";
                    font-size: 15px;
                    color: rgb(200,0,0);
                    text-shadow: 0.1em 0.1em black;
                    
                }

                .special2 { 
                    font-family: "Dingbats", Quivira, "Arial Unicode MS", Symbola, " Everson Mono";
                    font-size: 25px;
                    text-shadow: 0.05em 0.05em black;
                    color: rgb(200,0,0);
                }

                .bro {
                    color: rgb(200,0,0);
                    text-shadow: 1px 1px black;
                }

                .shadow {
                    box-shadow: 0px 5px 4px rgba(0,0,0, 0.1);
                    padding: 20px;
                    margin: 20px 0px 0px 0px;
                    min-width: 40%;


                }
                .hidden {
                font-size: 0px;
                }
                .center {
                    text-align: center;
                    font-family: helvetica, arial, sans-serif;
                    color: white;
                }
                
                .black {
                    background-color: rgba(40,40,40,0.5);
                    border-radius: 25px;

                }
                
                .white {
                    background-color: rgba(255,255,255,0);
                    padding-top: 10px;
                    padding-bottom: 25px;
                    padding-right: 10px;
                    padding-left: 10px; 
                    margin-top: 20px;

                    border-radius: 25px;
                    }

                </style>
                </head>
                <body>

    """
    return html