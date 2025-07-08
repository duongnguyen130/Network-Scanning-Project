<template>
  <div>
    <h2>Device Discovery Results</h2>
    <ul>
      <li v-for="host in results" :key="host.host">{{ host.host }}</li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const results = ref([])

onMounted(async () => {
  const res = await axios.get('/api/ping-scan/')
  results.value = res.data.hosts || []
})
</script>