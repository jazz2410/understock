<script>
	import { page } from '$app/stores';
	import { onDestroy, onMount } from 'svelte';
	import {
		Table,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell,
		Checkbox
	} from 'flowbite-svelte';
  import { Card } from 'flowbite-svelte';

	let ticker;
	let userData;
	let stockData = [];

	//Get the ticker symbol from URL
	const unsubscribe = page.subscribe(($page) => {
		ticker = $page.params.ticker;
	});

	onMount(async () => {
		try {
			const response = await fetch(`http://localhost:8000/stock/${ticker}`);
			stockData = await response.json();
		} catch (e) {
			console.error('Error fetching stock data:', e);
		}
	});

	function formatNumber(value) {
		if (value === undefined || value === null) return '-'; // Handle undefined values
		return new Intl.NumberFormat('en-US', {
			minimumFractionDigits: 2,
			maximumFractionDigits: 2
		}).format(value / 1_000_000); // Divide by 1 million and format
	}
</script>

<Card>
	<h1 class="text-2xl font-bold text-white">
		{stockData.length > 0 ? stockData[0].stockName : 'Loading...'}
		({stockData.length > 0 ? stockData[0].ticker : 'Loading...'})
	</h1>
  <h1 class="text-1xl font-semibold text-white" >
    Historic growth rate [%]: {stockData.length > 0 ? ( stockData[0].historic_fcf_growth * 100 ).toFixed(2) : 'Loading...'}
  </h1>
  <h1 class="text-1xl font-semibold text-white" >
    Calculated future growth rate [%]: {stockData.length > 0 ? ( stockData[0].future_fcf_growth * 100 ).toFixed(2) : 'Loading...'}
  </h1>
</Card>

<div class="item-center flex justify-center mt-1">

</div>

<div class="item-center flex justify-center mt-1">
	<Table hoverable={true} striped={true}>
		<TableHead>
			<TableHeadCell class="!p-4"></TableHeadCell>
			<TableHeadCell>Latest CF</TableHeadCell>
			<TableHeadCell>Latest CF +1 years</TableHeadCell>
			<TableHeadCell>Latest CF +2 years</TableHeadCell>
			<TableHeadCell>Latest CF +3 years</TableHeadCell>
			<TableHeadCell>Latest CF +4 years</TableHeadCell>
      <TableHeadCell>Latest CF +5 years</TableHeadCell>
      <TableHeadCell>Termination value</TableHeadCell>
		</TableHead>
		<TableBody tableBodyClass="divide-y">
			<TableBodyRow>
				<TableBodyCell class="!p-4">FCF</TableBodyCell>
				<TableBodyCell>{stockData.length > 0 ? formatNumber(stockData[0].last_cf) : 'Loading...'}</TableBodyCell>
				<TableBodyCell>{stockData.length > 0 ? formatNumber(stockData[0].fcf_1)   : 'Loading...'}</TableBodyCell>
				<TableBodyCell>{stockData.length > 0 ? formatNumber(stockData[0].fcf_2)   : 'Loading...'}</TableBodyCell>
				<TableBodyCell>{stockData.length > 0 ? formatNumber(stockData[0].fcf_3)   : 'Loading...'}</TableBodyCell>
				<TableBodyCell>{stockData.length > 0 ? formatNumber(stockData[0].fcf_4)   : 'Loading...'}</TableBodyCell>
        <TableBodyCell>{stockData.length > 0 ? formatNumber(stockData[0].fcf_5)   : 'Loading...'}</TableBodyCell>
        <TableBodyCell>{stockData.length > 0 ? formatNumber(stockData[0].fcf_6)   : 'Loading...'}</TableBodyCell>
			</TableBodyRow>
			<TableBodyRow>
				<TableBodyCell class="!p-4">DCF</TableBodyCell>
				<TableBodyCell>-</TableBodyCell>
				<TableBodyCell>{stockData.length > 0 ? formatNumber(stockData[0].dcf_1)   : 'Loading...'}</TableBodyCell>
				<TableBodyCell>{stockData.length > 0 ? formatNumber(stockData[0].dcf_2)   : 'Loading...'}</TableBodyCell>
				<TableBodyCell>{stockData.length > 0 ? formatNumber(stockData[0].dcf_3)   : 'Loading...'}</TableBodyCell>
				<TableBodyCell>{stockData.length > 0 ? formatNumber(stockData[0].dcf_4)   : 'Loading...'}</TableBodyCell>
        <TableBodyCell>{stockData.length > 0 ? formatNumber(stockData[0].dcf_5)   : 'Loading...'}</TableBodyCell>
        <TableBodyCell>{stockData.length > 0 ? formatNumber(stockData[0].dcf_6)   : 'Loading...'}</TableBodyCell>
			</TableBodyRow>
			<TableBodyRow>
				<TableBodyCell class="!p-4">Fair value</TableBodyCell>
				<TableBodyCell></TableBodyCell>
				<TableBodyCell></TableBodyCell>
				<TableBodyCell></TableBodyCell>
				<TableBodyCell></TableBodyCell>
				<TableBodyCell></TableBodyCell>
        <TableBodyCell></TableBodyCell>
        <TableBodyCell>{stockData.length > 0 ? formatNumber(stockData[0].fairValue)   : 'Loading...'}</TableBodyCell>
			</TableBodyRow>
		</TableBody>
	</Table>
</div>
<div class="item-center flex justify-center mt-3">
<p style="font-size: 0.9em; color: gray;">Numbers are in millions and USD.</p>
</div>