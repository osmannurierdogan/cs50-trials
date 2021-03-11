document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('form').onsubmit = () => {
        fetch('https://api.exchangeratesapi.io/latest?base=USD')
        .then(response => response.json()) // return response.json()
        .then(data => {
            const currencyType = document.querySelectorAll('.currency').value;
            const currencyBalance = document.querySelector('#currency').value;
            const rate = data.rates[currencyType];
            const balance = currencyBalance * rate;
            if (rate !== undefined){
                document.querySelector('#result').innerHTML = `${currencyBalance} ${currencyType} = ${balance.toFixed(3)} ${currencyType}.`;
            } else {
                document.querySelector('#result').innerHTML = 'Invalid Currency.'
            }
        })
        .catch(error => {
            console.log('Error : ', error);
        });
        return false;
    };    
});
