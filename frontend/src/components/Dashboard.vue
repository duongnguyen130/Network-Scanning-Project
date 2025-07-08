<template>
  <div>
    <h2 class="text-2xl font-bold mb-6">Dashboard</h2>
    <div class="grid grid-cols-2 gap-4">
      <div class="bg-white p-6 rounded shadow">
        <h3 class="font-semibold text-lg mb-2">Device Discovery</h3>
        <p>Discover all live hosts in your network</p>
        <router-link to="/device-discovery">
          <button class="mt-4 bg-blue-600 text-white px-4 py-2 rounded">Start Discovery</button>
        </router-link>
      </div>
      <div class="bg-white p-6 rounded shadow">
        <h3 class="font-semibold text-lg mb-2">Detailed Scan</h3>
        <p>Discover all devices in your network</p>
        <router-link to="/detailed-scan">
          <button class="mt-4 bg-blue-600 text-white px-4 py-2 rounded">Start Discovery</button>
        </router-link>
      </div>
    </div>
  </div>
</template>