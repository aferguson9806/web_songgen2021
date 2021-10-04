localStorage.clear();
const songForm = document.querySelector('.songForm');
const choice = document.getElementsByName('instrument');
const songName = document.getElementById('songname');
const songKey = document.getElementById('keySelect');
const songDuration = document.getElementById('duration')
const screenDiv = document.getElementsByClassName('container')



function findChecked() {
    for (let i=0; i<choice.length; i++) {
        if (choice[i].checked) {
            return(choice[i]);
        }
    }
}


songForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    //console.log(duration.value);
    localStorage.setItem('instrument', findChecked().value)
    localStorage.setItem('songName', songName.value);
    localStorage.setItem('songKey', songKey.options[songKey.selectedIndex].text);
    localStorage.setItem('songDuration', songDuration.value);

    console.log(localStorage)
    songForm.reset();
    
    await fetch('/song')
});