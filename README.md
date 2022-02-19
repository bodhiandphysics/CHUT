# CHUT Transit App

This is the main repo for the CHUT Transit App by CHUT for Calgary Hacks 2022.

## Cloning the repo

```bash
git clone git@github.com:bodhiandphysics/CHUT.git
```

## Starting the app

The backend is done with django. To run the webserver change directory into `CHUT/` and type:
```bash
python manage.py runserver
```
This will start the server on the address [127.0.0.1:8000](http://127.0.0.1:8000).

To view the app go to [127.0.0.1:8000/transit](http://127.0.0.1:8000/transit).

## Launching the virtual environnment

On microsoft
```bash
PATH\CHUT>CHUT.venv\Scripts\activate
```

On linux
```bash
bash -c "source .venv/bin/activate"
```

Install packages:
```bash
python3 -m pip install -r .venv/requirements.txt
```

# TODO

- [x] Get Repo set up
- [x] Start django project and server
- [x] Setup python virtual environment
- [ ] Build UI
- [ ] Parse Data
- [ ] Display information on site
- [ ] Integrate into Pi




