<template>
  <div>
    <h2>Dashboard</h2>
    <div class="buttons">
      <button @click="startPingScan">🔍 Discover Devices</button>
      <button @click="startDetailedScan">🔬 Detailed Discovery</button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()

const startPingScan = async () => {
  await axios.get('/api/ping-scan/')
  router.push('/discovery')
}

const startDetailedScan = async () => {
  await axios.get('/api/detailed-scan/')
  router.push('/detailed')
}
</script>

<style scoped>
.buttons {
  display: flex;
  gap: 1rem;
}
button {
  padding: 0.5rem 1rem;
  font-size: 16px;
}
</style>