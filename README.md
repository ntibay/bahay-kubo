# bahay-kubo
Boilerplate of Graphene workshop for Pycon APAC 2019.

## Setup Requirements
* Internet :satisfied:

You should have this installed prior to the workshop:
* Python3 (Bundled with the `venv` module to create virtual environments)
* git
* Editor

## Setup
1. Create the project directory
```
mkdir graphene-tutorial
cd graphene-tutorial
```

2. Create a virtual environment
```
python3 -m venv env3

On Windows:
py -3 -m venv env3
```

3. Activate the environment
```
source env3/bin/activate

On Windows:
source env3\Scripts\activate
```

4. Clone the `bahay-kubo` :house_with_garden: project from Github
```
git clone https://github.com/neequole/bahay-kubo.git
```

5. Go to the boilerplate folder
```
cd bahay-kubo
```

6. Install requirements
```
pip install -r requirements.txt
```

7. Run and check if the project is running!
```
python app.py

Output:
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) <------ Open the link on your browser
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 262-544-471
```

## Say hello to Mang Netong!

1. Go to the `graphql` endpoint which is like http://127.0.0.1:5000/graphql
2. Type in the ff. and say hello :wave: to Mang Netong!
```
{
  hello
}
```
