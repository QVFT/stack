# stack
website v2.

📐 [Emoji policy](http://greena13.github.io/blog/2016/08/19/emojis-are-the-solution-to-useless-commit-messages/) for commit, issues, and PRs. 


# Team Members

- Michael Wrana
- Chris Molloy
- Ryan Power
- Carter Conboy
- Quantum Hu

# Running Website

* Clone the repo
* Start QVFT conda env
* Import requirements

```pip install -r requirements.txt```

If you are having an issue with loading psyco2 run

```brew install postgresqld```
* Run flask server
```
cd web/local_ser

export FLASK_APP=flaskr
    
export FLASK_ENV=development

flask run
