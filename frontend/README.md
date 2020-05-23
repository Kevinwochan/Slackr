# How to run the frontend

## On CSE Machines

```bash
sh install.sh
sh run.sh [BACKEND PORT] [FRONTEND PORT]
```

For example:

```bash
sh install.sh
sh run.sh 5000 3000
```

The backend port is just an integer that is the port the flask server is CURRENTLY running on. The frontend port is the port you want your frontend to run on.

## On your own machine

```bash
cp package-local.json package.json
npm install
./run.sh [BACKEND PORT] [FRONTEND PORT]
```

The backend port is just an integer that is the port the flask server is CURRENTLY running on. The frontend port is the port you want your frontend to run on.
