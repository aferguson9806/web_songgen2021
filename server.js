// These are our required libraries to make the server work.
/* eslint-disable no-console */
/* eslint-disable no-unused-vars */

import require from 'requirejs';
let {PythonShell} = require('python-shell'); 



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
});
