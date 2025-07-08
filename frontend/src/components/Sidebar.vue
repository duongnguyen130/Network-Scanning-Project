<template>
  <nav class="sidebar">
    <ul>
      <li><router-link to="/">Dashboard</router-link></li>
      <li><router-link to="/discovery">Device Discovery</router-link></li>
      <li><router-link to="/detailed">Detailed Scan</router-link></li>
    </ul>
  </nav>
</template>

<style scoped>
.sidebar {
  width: 200px;
  background-color: #2c3e50;
  color: white;
  height: 100vh;
  padding: 1rem;
}
.sidebar ul {
  list-style: none;
  padding: 0;
}
.sidebar li {
  margin: 1rem 0;
}
.sidebar a {
  color: white;
  text-decoration: none;
}
.sidebar a.router-link-active {
  font-weight: bold;
}
</style>
