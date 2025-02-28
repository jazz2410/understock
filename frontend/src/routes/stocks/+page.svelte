<script lang="js">
	import { onMount } from 'svelte';
	import {
		Table,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell,
		Checkbox,
		TableSearch
	} from 'flowbite-svelte';
	import { goto } from '$app/navigation';
	import Footer from '$lib/Footer.svelte';
	let items = [];

	let selectedEvaluation = 'DCF';

	onMount(async () => {
		try {
			const response = await fetch('http://localhost:8000/stocks');
			//const response = await fetch('/api/stocks');
			items = await response.json();
			console.log(items);
		} catch (error) {
			console.error('Error fetching stocks:', error);
		}
	});
</script>

<div class="flex items-center justify-center">
	<div class="w-full max-w-6xl overflow-x-auto">
		{#if items.length}
			<p class="mb-4 text-center text-sm text-gray-400">
				📅 Table was updated on {items[0].timestamp}
			</p>
			<p class="text-center my-2">Click on the ticker symbol or stock name to see the evaluation</p>
			<p class="text-center my-2">Delta is the percentage difference between last price and fair value</p>
			<p class="text-center my-2">Click on the delta column header to sort by highest delta</p>
			<div class="mt-5 flex items-center justify-center">
				<button on:click={() => { selectedEvaluation = 'DCF' }}
					class="mx-3 my-1 transform cursor-pointer rounded-lg border border-white bg-black px-6 py-5 font-semibold text-black
               shadow-md transition duration-300 ease-in-out hover:scale-105 hover:bg-orange-600 focus:outline-none
                focus:ring-2 dark:text-white" class:!bg-orange-500={selectedEvaluation === 'DCF'}>DCF evaluation</button
				>
				<button on:click={() => { selectedEvaluation = 'Graham' }}
					class="my-1 transform cursor-pointer rounded-lg border border-white bg-black px-6 py-5 font-semibold text-black
				shadow-md transition duration-300 ease-in-out hover:scale-105 hover:bg-orange-600 focus:outline-none
				 focus:ring-2 dark:text-white" class:!bg-orange-500={selectedEvaluation === 'Graham'}>Graham evaluation</button
				>
			</div>
			<div class="flex justify-center">
				<button on:click={() => { selectedEvaluation = 'Compare' }}
					class="my-1 transform cursor-pointer rounded-lg border border-white bg-black px-6 py-5 font-semibold text-black
				shadow-md transition duration-300 ease-in-out hover:scale-105 hover:bg-orange-600 focus:outline-none
				 focus:ring-2 dark:text-white" class:!bg-orange-500={selectedEvaluation === 'Compare'}>Compare evaluation</button
				>
			</div>

			{#if selectedEvaluation == 'DCF'}
				<Table
					{items}
					striped={true}
					placeholder="Search by ticker or stock name"
					hoverable={true}
					filter={(item, searchTerm) =>
						item.ticker.toLowerCase().includes(searchTerm.toLowerCase()) ||
						item.stockName.toLowerCase().includes(searchTerm.toLowerCase())}
					class="rounded-2xl"
					color="black"
				>
					<TableHead class="rounded-t-2xl">
						<TableHeadCell
							class="text-white"
							sort={(a, b) => a.ticker.localeCompare(b.ticker)}
							defaultSort>TICKER</TableHeadCell
						>
						<TableHeadCell class="text-white">Stock name</TableHeadCell>
						<TableHeadCell class="text-white">Last price [USD]</TableHeadCell>
						<TableHeadCell class="text-white">Fair value [USD] (DCF)</TableHeadCell>
						<TableHeadCell
							class="text-white"
							sort={(a, b) => a.delta - b.delta}
							defaultDirection="desc">DELTA [%] (DCF)</TableHeadCell
						>
					</TableHead>
					<TableBody tableBodyClass="divide-y">
						<TableBodyRow slot="row" let:item>
							<TableBodyCell>
								<button
									on:click={() => window.open(`/stock/${item.ticker}`,'_blank')}
									class="h-10 w-20 cursor-pointer hover:bg-orange-400"
								>
									{item.ticker}
								</button>
							</TableBodyCell>

							<TableBodyCell>
								<button
									on:click={() => window.open(`/stock/${item.ticker}`,'_blank')}
									class="h-10 w-full cursor-pointer hover:bg-orange-400"
								>
									{item.stockName}
								</button>
							</TableBodyCell>
							<TableBodyCell>{item.lastPrice}</TableBodyCell>
							<TableBodyCell><div class="px-3 py-3"  
												class:!bg-red-500={item.fairValueShare < item.lastPrice} 
											    class:!bg-green-700={item.fairValueShare > item.lastPrice}>{item.fairValueShare}</div></TableBodyCell>
							<TableBodyCell>{item.delta}</TableBodyCell>
						</TableBodyRow>
					</TableBody>
				</Table>
			{:else if selectedEvaluation == 'Graham'}
				<Table
					{items}
					striped={true}
					placeholder="Search by ticker or stock name"
					hoverable={true}
					filter={(item, searchTerm) =>
						item.ticker.toLowerCase().includes(searchTerm.toLowerCase()) ||
						item.stockName.toLowerCase().includes(searchTerm.toLowerCase())}
					class="rounded-2xl"
					color="black"
				>
					<TableHead class="rounded-t-2xl">
						<TableHeadCell
							class="text-white"
							sort={(a, b) => a.ticker.localeCompare(b.ticker)}
							defaultSort>TICKER</TableHeadCell
						>
						<TableHeadCell class="text-white">Stock name</TableHeadCell>
						<TableHeadCell class="text-white">Last price [USD]</TableHeadCell>
						<TableHeadCell class="text-white">Fair value [USD] (Graham)</TableHeadCell>
						<TableHeadCell
							class="text-white"
							sort={(a, b) => a.delta_graham - b.delta_graham}
							defaultDirection="desc">DELTA [%] (Graham)</TableHeadCell
						>
					</TableHead>
					<TableBody tableBodyClass="divide-y">
						<TableBodyRow slot="row" let:item>
							<TableBodyCell>
								<button
									on:click={() => window.open(`/stock/${item.ticker}`,'_blank')}
									class="h-10 w-20 cursor-pointer hover:bg-orange-400"
								>
									{item.ticker}
								</button>
							</TableBodyCell>

							<TableBodyCell>
								<button
									on:click={() => window.open(`/stock/${item.ticker}`,'_blank')}
									class="h-10 w-full cursor-pointer hover:bg-orange-400"
								>
									{item.stockName}
								</button>
							</TableBodyCell>
							<TableBodyCell>{item.lastPrice}</TableBodyCell>
							<TableBodyCell><div class="px-3 py-3"  
								class:!bg-red-500={item.fairValueGraham < item.lastPrice} 
								class:!bg-green-700={item.fairValueGraham > item.lastPrice}>
								{item.fairValueGraham}</div></TableBodyCell>
							<TableBodyCell>{item.delta_graham}</TableBodyCell>
						</TableBodyRow>
					</TableBody>
				</Table>
			{:else}
			<Table
			{items}
			striped={true}
			placeholder="Search by ticker or stock name"
			hoverable={true}
			filter={(item, searchTerm) =>
				item.ticker.toLowerCase().includes(searchTerm.toLowerCase()) ||
				item.stockName.toLowerCase().includes(searchTerm.toLowerCase())}
			class="rounded-2xl"
			color="black"
		>
			<TableHead class="rounded-t-2xl">
				<TableHeadCell
					class="text-white"
					sort={(a, b) => a.ticker.localeCompare(b.ticker)}
					defaultSort>TICKER</TableHeadCell
				>
				<TableHeadCell class="text-white">Stock name</TableHeadCell>
				<TableHeadCell class="text-white">Last price [USD]</TableHeadCell>
				<TableHeadCell class="text-white">Fair value [USD] (DCF)</TableHeadCell>
				<TableHeadCell class="text-white">Fair value [USD] (Graham)</TableHeadCell>				
				<TableHeadCell
					class="text-white"
					sort={(a, b) => a.delta - b.delta}
					defaultDirection="desc">DELTA [%] (DCF)</TableHeadCell>

				<TableHeadCell
					class="text-white"
					sort={(a, b) => a.delta_graham - b.delta_graham}
					defaultDirection="desc">DELTA [%] (Graham)</TableHeadCell>

			</TableHead>
			<TableBody tableBodyClass="divide-y">
				<TableBodyRow slot="row" let:item>
					<TableBodyCell>
						<button
							on:click={() => window.open(`/stock/${item.ticker}`,'_blank')}
							class="h-10 w-20 cursor-pointer hover:bg-orange-400"
						>
							{item.ticker}
						</button>
					</TableBodyCell>

					<TableBodyCell>
						<button
							on:click={() => window.open(`/stock/${item.ticker}`,'_blank')}
							class="h-10 w-full cursor-pointer hover:bg-orange-400"
						>
							{item.stockName}
						</button>
					</TableBodyCell>
					<TableBodyCell>{item.lastPrice}</TableBodyCell>
					<TableBodyCell>
						<div class="px-3 py-3"  
								class:!bg-red-500={item.fairValueShare < item.lastPrice} 
								class:!bg-green-700={item.fairValueShare > item.lastPrice}>
								{item.fairValueShare}</div>
						</TableBodyCell>
					<TableBodyCell>
						<div class="px-3 py-3"  
						class:!bg-red-500={item.fairValueGraham < item.lastPrice} 
						class:!bg-green-700={item.fairValueGraham > item.lastPrice}>
						{item.fairValueGraham}</div>
						</TableBodyCell>
					<TableBodyCell>{item.delta}</TableBodyCell>
					<TableBodyCell>{item.delta_graham}</TableBodyCell>
				</TableBodyRow>
			</TableBody>
		</Table>
			{/if}
		{:else}
			<p>Loading data...</p>
		{/if}
	</div>
</div>

<Footer></Footer>
