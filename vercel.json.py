{
    "builds " :[{
    "src": "onlineexam/wsgi.py" ,
    "use": "@vercel/python",

    "config": { "maxLambdaSize":"15 mb","runtime": "python3.11"}
}],
" routes " :[
        {
            "src":"/(.*)",
            "dest":"onlineexam/wsgi.py",
        }
    ]
}