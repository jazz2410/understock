<script lang="ts">
    import { onMount } from 'svelte';
    let data = [];
  
    async function fetchData() {
      try {
        const res = await fetch('http://localhost:8000');
        if (!res.ok) throw new Error('Failed to fetch data');
        data = await res.json();
        console.log(data[1]);
      } catch (error) {
      }
    }
  
    onMount(fetchData);
  </script>

<div class="flex items-center justify-center">

<h1 class="underline">Understocks</h1>




</div> 
<div class="flex item-center justify-center">
<table class="table-auto border-collapse border border-gray-300  mt-5">
    <thead>
      <tr class="bg-gray-200">
        <th class="border border-gray-300 px-4 py-2">Ticker</th>
        <th class="border border-gray-300 px-4 py-2">Last price in USD</th>
      </tr>
    </thead>
    <tbody>
      {#each data as item}
        <tr class="hover:bg-gray-100">
          <td class="border border-gray-300 px-4 py-2">{item.ticker}</td>
          <td class="border border-gray-300 px-4 py-2">{item.lastPrice}</td>
        </tr>
      {/each}
    </tbody>
</table>
</div>