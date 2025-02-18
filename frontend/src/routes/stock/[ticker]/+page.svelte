<script>
  import { page } from "$app/stores";
  import { onDestroy } from "svelte";

  let ticker;
  let userData;

    // Subscribe to the route parameters
    const unsubscribe = page.subscribe(($page) => {
    ticker = $page.params.ticker;
    console.log(ticker)
});


</script>


