"use client";

import { useEffect } from "react";
import { Button } from "@/components/ui/button"; // if using shadcn
import { Loader2 } from "lucide-react"; // optional for spinner
import { useState } from "react";

export default function LoginPage() {
  const [loading, setLoading] = useState(false);

  const handleGoogleLogin = async () => {
    setLoading(true);
    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/auth/google/authorize`, {
        credentials: "include",
      });

      const data = await res.json();
      if (res.ok && data.authorization_url) {
        window.location.href = data.authorization_url;
      } else {
        console.error("Failed to get Google OAuth URL:", data);
      }
    } catch (error) {
      console.error("Login failed:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <h1 className="text-3xl font-bold mb-6">Sign in to Aletheia</h1>
      <Button onClick={handleGoogleLogin} disabled={loading}>
        {loading ? <Loader2 className="animate-spin mr-2" /> : null}
        Continue with Google
      </Button>
    </div>
  );
}
