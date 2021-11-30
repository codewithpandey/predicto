chrome.runtime.sendMessage({ todo: "showPageAction" });

loadCount = 0;

window.addEventListener('DOMFocusIn', function () {

   

    // console.clear();

    let reviewContainer = document.querySelector('textarea._3kRe7w');
    let stars = [];

    document.querySelector('._2teBVu')
        .childNodes
        .forEach(child => stars.push(child));

    stars.reverse();
    stars.unshift(0);

    reviewContainer.addEventListener('keyup', function (e) {

        let review = e.target.value;

        if (review.includes('awesome')) updateRating(5);
        if (review.includes('amazing')) updateRating(5);
        if (review.includes('decent')) updateRating(3);
        if (review.includes('great')) updateRating(4);
        if (review.includes('worst')) updateRating(1);
        if (review.includes('cool')) updateRating(3);
        if (review.includes('nice')) updateRating(4);
        if (review.includes('bad')) updateRating(1);

    });

    String.prototype.includes = function (keyword) {
        return this.split(' ').includes(keyword) ? true : false;
    }

    function updateRating(digit) {

        if (digit == undefined || digit == null) return;
        if (digit < 1 || digit > 5) return console.error('rating not within the range 1 to 5');
        if (!Number.isInteger(digit)) return console.error(`rating must be an Integer, recieved ${typeof digit}!`)

        stars[digit].click();
    }

    if(loadCount == 0) {

        ratingContainer = document.querySelector('._14YOVU');

        progressBarContainer = document.createElement('div');
        progressBarContainer.setAttribute('data-progress', '80');
        progressBarContainer.setAttribute('class', 'progressBarContainer');

        progressBar = document.createElement('div');
        progressBar.setAttribute('data-progress', '80');
        progressBar.setAttribute('class', 'progressBar');

        ratingContainer.appendChild(progressBarContainer);
        document.querySelector('.progressBarContainer').appendChild(progressBar);

        messageContainer = document.createElement('span');
        messageContainer.setAttribute('class', 'messageContainer');
        messageContainer.innerHTML = 'Your rating is 80% positive. 👍';
        ratingContainer.appendChild(messageContainer);




        loadCount++;
    }
   

}, false);
