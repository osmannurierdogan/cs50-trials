
if(!localStorage.getItem('counter')){
    localStorage.setItem('counter', 0);
}

let count = () => {
    let counter = localStorage.getItem('counter');
    counter++;
    //console.log(counter);
    document.querySelector('h1').innerHTML = counter;
    /* if (counter % 10 === 0) {
        alert(`Count is now ${counter}`);
    } */
    localStorage.setItem('counter', counter);
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    document.querySelector('button').onclick = count;
    // setInterval(count, 1000);
});