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

/* function download() {
  let element = document.createElement('button');
  element.innerHTML = "Download";
  downDiv.appendChild(element)

} */


songForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const data = {'instrument': findChecked().value, 'songName': songName.value.replace(/\s/g, ""), 'songKey': songKey.options[songKey.selectedIndex].value, 'songDuration': songDuration.value};
    console.log(data);


    //console.log(localStorage)
    songForm.reset();
    //console.log(JSON.stringify(data));
    await fetch("/song", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
          },
        body: JSON.stringify(data)
      }).then(res => {
        console.log("Request complete! response:", res);
      });

    const newLink = document.createElement('a');
    newLink.href = "out_songs/" + songName.value.replace(/\s/g, "") + ".wav"
    newLink.download = songName.value.replace(/\s/g, "") + ".wav"
    document.body.appendChild(newLink);
    newLink.click();
    newLink.remove();
});

