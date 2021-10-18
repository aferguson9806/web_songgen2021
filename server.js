// These are our required libraries to make the server work.
/* eslint-disable no-console */
/* eslint-disable no-unused-vars */
import express from 'express';
import dotenv from 'dotenv';
import PythonShell from 'python-shell';

dotenv.config();

const app = express();
const port = process.env.PORT || 8000;

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

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
};

app.route('/results')
  .post(async (req, res) => {
    console.log('POST request detected');
    console.log('Form data in res.body', req.body);
    console.log('Now send something back to your client');


    res.send({data: req.body})
  });




app.route('/song')
.post(async (req, res) => {
  //console.log(req.body.songDuration);
  console.log(typeof(req.body.instrument));
  console.log(typeof(req.body.songName));
  console.log(typeof(req.body.songKey));
  console.log(typeof(parseInt(req.body.songDuration)));
  
  let options = {
    //scriptPath: 'Users/aferg/OneDrive/Documents/GitHub/web_songgen2021/public/',
    args: [req.body.instrument, req.body.songName, req.body.songKey, parseInt(req.body.songDuration)]
  };

  PythonShell.run('public/songgenv2.py', options, function (err, results) {
    if (err) throw err;
    console.log('results: %j', results);
  });

  await sleep(((req.body.songDuration * 1000) * 2) + 4000);

  let optionsClear = {
    args: ['public/out_songs/' + req.body.songName + '.wav']
  }

  PythonShell.run('public/clear.py', optionsClear, function (errClear, resultsClear) {
    if (errClear) throw errClear;
    console.log("file cleared", resultsClear)
  })
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}!`);
});
