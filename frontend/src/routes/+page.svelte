<script lang="js">
import { onMount } from 'svelte';

export let data;

async function updateData(){
    data.data[1].lastPrice = '100';
    
        for(const stock of data.data){

        console.log(stock);
        console.log(stock.ticker)
        const symbol = stock.ticker;  // Replace with the stock symbol you want, e.g., 'AAPL' for Apple
        const url = `https://query1.finance.yahoo.com/v8/finance/chart/${symbol}?range=1d&interval=1m`; 
    
        const response = await fetch(url);
        const data = await response.json();
        const price = data.chart.result[0].meta.regularMarketPrice;
        console.log(price);
        }

        

}

onMount(() => {
        const interval = setInterval(updateData, 5000);
        return () => clearInterval(interval); // Cleanup on unmount
    });

</script>

<div class="flex items-center justify-center">

<h1 class="underline">Understocks</h1>

</div> 
<div class="flex item-center justify-center">
<table class="table-auto border-collapse border border-gray-300  mt-5">
    <thead>
      <tr class="bg-gray-200">
        <th class="border border-gray-300 px-4 py-2">Ticker</th>
        <th class="border border-gray-300 px-4 py-2">Stock name</th>
        <th class="border border-gray-300 px-4 py-2">Last price in USD</th>
        <th class="border border-gray-300 px-4 py-2">Fair value</th>
      </tr>
    </thead>
    <tbody>
      {#each data.data as item}
        <tr class="hover:bg-gray-100">
          <td class="border border-gray-300 px-4 py-2">{item.ticker}</td>
          <td class="border border-gray-300 px-4 py-2">{item.stockName}</td>
          <td class="border border-gray-300 px-4 py-2">{item.lastPrice}</td>
          <td class="border border-gray-300 px-4 py-2">{item.fairValue}</td>
        </tr>
      {/each}
    </tbody>
</table>
</div>