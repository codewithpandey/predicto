loadCount = 0;
chrome.runtime.sendMessage({ todo: "showPageAction" });

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
        if (review.includes('worst')) updateRating(1);
        if (review.includes('great')) updateRating(4);
        if (review.includes('cool')) updateRating(3);
        if (review.includes('nice')) updateRating(2);
        if (review.includes('bad')) updateRating(1);

    });

    String.prototype.includes = function (keyword) {
        return this.split(' ').includes(keyword) ? true : false;
    }

    function updateRating(rating) {

        if (
            rating == undefined ||
            rating == null ||
            rating < 1 ||
            rating > 5 ||
            !Number.isInteger(rating)
        ) return;

        stars[rating].click();
        updateProgressBar(rating);
        updateProgressBarMessage(rating)

    }

    function updateProgressBarMessage(rating) {
        let messageContainer = document.querySelector('.messageContainer');
        messageContainer.innerHTML = `Your rating is ${rating * 20}% positive. 👍`;
    }

    function updateProgressBar(rating) {
        let progressBar = document.querySelector('.progressBar');
        progressBar.style.width = `${rating * 20}%`;
    }


    if (loadCount == 0) {

        ratingContainer = document.querySelector('._14YOVU');

        progressBarContainer = document.createElement('div');
        progressBarContainer.setAttribute('data-progress', '80');
        progressBarContainer.setAttribute('class', 'progressBarContainer');

        progressBar = document.createElement('div');
        progressBar.setAttribute('data-progress', '80');
        progressBar.setAttribute('class', 'progressBar');

        messageContainer = document.createElement('span');
        messageContainer.setAttribute('class', 'messageContainer');
        messageContainer.innerHTML = `Start typing to see analysis of your review.`;

        ratingContainer.appendChild(progressBarContainer);
        progressBarContainer.appendChild(progressBar);
        ratingContainer.appendChild(messageContainer);

        loadCount++;
    }

}, false);
