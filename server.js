// These are our required libraries to make the server work.
/* eslint-disable no-console */
/* eslint-disable no-unused-vars */
import express from 'express';
import dotenv from 'dotenv';
import fetch from 'node-fetch';
import child_process from 'child_process';

dotenv.config();

const app = express();
const port = process.env.PORT || 3000;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(express.static('public'));

app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
  next();
});


/* app.route('/api')
  .get(async (req, res) => {
    console.log('GET request detected');
    const data = await fetch('https://data.princegeorgescountymd.gov/resource/umjn-t2iz.json');
    const json = await data.json();
    console.log('data from fetch', json);
    res.json(json);
  })
  .post(async (req, res) => {
    console.log('POST request detected');
    console.log('Form data in res.body', req.body);
    console.log('Now send something back to your client');

    const data = await fetch('https://data.princegeorgescountymd.gov/resource/umjn-t2iz.json');
    const json = await data.json();

    res.json({ data: json })
  }); */

app.route('/results')
  .post(async (req, res) => {
    console.log('POST request detected');
    console.log('Form data in res.body', req.body);
    console.log('Now send something back to your client');


    res.send({data: req.body})
  });


app.route('/song')
.get(async (req, res) => {
  console.log(req.query);
  const python = child_process.spawn('py', ['public/songgenv2.py', localStorage.getItem("instrument"), localStorage.getItem("songName"), localStorage.getItem("songKey"), localStorage.getItem("songDuration")]);
  python.stdout.on('data', function (data) {
    console.log('Pipe data from python script ...');
    });
  python.on('close', (code) => {
    console.log(`child process close all stdio with code ${code}`);
    // send data to browser
    });
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}!`);
});
