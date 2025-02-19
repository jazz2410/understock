<script>
	import { page } from '$app/stores';
	import { onDestroy, onMount } from 'svelte';

	let ticker;
	let userData;
  let stockData = null;

  //Get the ticker symbol from URL
	const unsubscribe = page.subscribe(($page) => {
		ticker = $page.params.ticker;
	});

    onMount( async () => {
      try{
        const response = await fetch(`http://localhost:8000/stock/${ticker}`);
        stockData = await response.json();
        console.log(stockData)
      }
      catch(e){
        console.error("Error fetching stock data:", e);
      };
    } )
</script>

<div class="item-center flex justify-center">




</div>
