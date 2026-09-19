import { readFile } from "node:fs/promises";

// Node fetch does not support HTTP proxies directly. Use this example to load
// the list, then pass a selected proxy to your preferred proxy agent library.
const file = new URL("../../proxies/all/data.txt", import.meta.url);
const proxies = (await readFile(file, "utf8")).trim().split("\n");

console.log({
  selectedProxy: proxies[0],
  count: proxies.length,
});
