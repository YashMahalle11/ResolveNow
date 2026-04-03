import { Route, Routes } from "react-router-dom";

import Login from "../features/auth/Login";
import Register from "../features/auth/Register";
import LandingPage from "../features/home/LandingPage";
import VerifyEmail from "../features/auth/VerifyEmail";

function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/register" element={<Register />} />
      <Route path="/login" element={<Login />} />
      <Route path="/verify-email" element={<VerifyEmail />} />
    </Routes>
  );
}

export default AppRoutes;
