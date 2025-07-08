<template>
  <div class="dashboard">
    <div class="card">
      <h3>Device Discovery</h3>
      <p>Run a basic ping scan</p>
      <router-link to="/device-discovery">
        <button>START DISCOVERY</button>
      </router-link>
    </div>
    <div class="card">
      <h3>Detailed Scan</h3>
      <p>Run a detailed network scan</p>
      <button>START DETAIL SCAN</button>
    </div>
  </div>
</template>

<style scoped>
.dashboard {
  flex: 1;
  padding: 40px;
  background-color: #f7f8fa;
  display: flex;
  gap: 20px;
}

.card {
  background: white;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  width: 300px;
}

button {
  background-color: #3b82f6;
  color: white;
  border: none;
  padding: 10px;
  width: 100%;
  margin-top: 10px;
  border-radius: 8px;
  font-weight: bold;
}
</style>
