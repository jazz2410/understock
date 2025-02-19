<script>
	import { page } from '$app/stores';
	import { onDestroy, onMount } from 'svelte';
  import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell, Checkbox } from 'flowbite-svelte';
	let ticker;
	let userData;
  let stockData = [];

  //Get the ticker symbol from URL
	const unsubscribe = page.subscribe(($page) => {
		ticker = $page.params.ticker;
	});

    onMount( async () => {
      try{
        const response = await fetch(`http://localhost:8000/stock/${ticker}`);
        stockData = await response.json();
        console.log(stockData)
        console.log(stockData[0].ticker)
      }
      catch(e){
        console.error("Error fetching stock data:", e);
      };
    } )
</script>

<div class="item-center flex justify-center py-6">
  <h1>{stockData.length > 0 ? stockData[0].stockName : 'Loading...'} 
      ({stockData.length > 0 ? stockData[0].ticker : 'Loading...'})</h1>
</div>


<div class="item-center flex justify-center">
<Table hoverable={true} striped={true}>
  <TableHead>
    <TableHeadCell class="!p-4">
      
    </TableHeadCell>
    <TableHeadCell>Latest CF</TableHeadCell>
    <TableHeadCell>Latest CF +1 years</TableHeadCell>
    <TableHeadCell>Latest CF +2 years</TableHeadCell>
    <TableHeadCell>Latest CF +3 years</TableHeadCell>
    <TableHeadCell>Latest CF +4 years</TableHeadCell>
  </TableHead>
  <TableBody tableBodyClass="divide-y">
    <TableBodyRow>
      <TableBodyCell class="!p-4">
        FCF
      </TableBodyCell>
      <TableBodyCell>Apple Mac"</TableBodyCell>
      <TableBodyCell>Sliver</TableBodyCell>
      <TableBodyCell>Laptop</TableBodyCell>
      <TableBodyCell>$2999</TableBodyCell>
      <TableBodyCell>1000</TableBodyCell>
    </TableBodyRow>
    <TableBodyRow>
      <TableBodyCell class="!p-4">
        DCF
      </TableBodyCell>
      <TableBodyCell>Microsoft</TableBodyCell>
      <TableBodyCell>White</TableBodyCell>
      <TableBodyCell>Laptop PC</TableBodyCell>
      <TableBodyCell>$1999</TableBodyCell>
      <TableBodyCell>
        <a href="/tables" class="font-medium text-primary-600 hover:underline dark:text-primary-500">Edit</a>
      </TableBodyCell>
    </TableBodyRow>
    <TableBodyRow>
      <TableBodyCell class="!p-4">
        Result
      </TableBodyCell>
      <TableBodyCell>Magic </TableBodyCell>
      <TableBodyCell>Black</TableBodyCell>
      <TableBodyCell>Accessories</TableBodyCell>
      <TableBodyCell>$99</TableBodyCell>
      <TableBodyCell>
        <a href="/tables" class="font-medium text-primary-600 hover:underline dark:text-primary-500">Edit</a>
      </TableBodyCell>
    </TableBodyRow>
  </TableBody>
</Table>
</div>