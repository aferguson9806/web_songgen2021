import require from 'requirejs';
let {PythonShell} = require('python-shell');



localStorage.clear();
const songForm = document.querySelector('.songForm');
const choice = document.getElementsByName('instrument');
const songName = document.getElementById('songname');
const songKey = document.getElementById('keySelect');
const songDuration = document.getElementById('duration')
const screenDiv = document.getElementsByClassName('container')
const downDiv = document.querySelector(".myButton")



function findChecked() {
    for (let i=0; i<choice.length; i++) {
        if (choice[i].checked) {
            return(choice[i]);
        }
    }
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}


songForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const data = {'instrument': findChecked().value, 'songName': songName.value.replace(/\s/g, ""), 'songKey': songKey.options[songKey.selectedIndex].value, 'songDuration': songDuration.value};
    console.log(data);


    //console.log(localStorage)
    songForm.reset();

    PythonShell.run('public/songgenv2.py', data, function (err, results) {
      if (err) throw err;
      console.log('results: %j', results)
    })

    await sleep(500);

    const newLink = document.createElement('a');
    newLink.href = "out_songs/" + data.songName + ".wav";
    newLink.download = data.songName + ".wav";
    document.body.appendChild(newLink);
    newLink.click();
    newLink.remove();


});

