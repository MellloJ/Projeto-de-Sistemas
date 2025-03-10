// document.addEventListener("DOMContentLoaded", function() {
//     const svgElements = document.getElementsByClassName('svg_img_color');
//     Array.from(svgElements).forEach(svgElement => {
//         fetch(svgElement.src)
//             .then(response => response.text())
//             .then(data => {
//                 const parser = new DOMParser();
//                 const svgDoc = parser.parseFromString(data, 'image/svg+xml');
//                 const svgRoot = svgDoc.documentElement;

//                 const isDarkTheme = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
//                 const fillColor = isDarkTheme ? getComputedStyle(document.documentElement).getPropertyValue('--bg-dark').trim() : getComputedStyle(document.documentElement).getPropertyValue('--bg-white').trim();
//                 svgRoot.querySelector('path').setAttribute('fill', fillColor);

//                 Array.from(svgElement.attributes).forEach(attr => {
//                     svgRoot.setAttribute(attr.name, attr.value);
//                 });

//                 svgElement.parentNode.replaceChild(svgRoot, svgElement);
//             });
//     });
// });

document.addEventListener("DOMContentLoaded", function() {
    const baseColorVariable = '--base-color';
    const colors = [
        'rgb(255, 193, 7)', // #FFC107
        'rgb(255, 87, 34)', // #FF5722
        'rgb(76, 175, 80)', // #4CAF50
        'rgb(33, 150, 243)' // #2196F3
    ];
    let currentColorIndex = 0;

    function changeBaseColor() {
        document.documentElement.style.setProperty(baseColorVariable, colors[currentColorIndex]);
        currentColorIndex = (currentColorIndex + 1) % colors.length;
    }

    setInterval(changeBaseColor, 1000); // Change color every second
});