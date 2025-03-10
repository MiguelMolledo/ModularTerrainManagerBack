-- Create a table for projects
CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(50) CHECK (status IN ('Active', 'Completed', 'Pending'))
);

-- Create a table for tiles
CREATE TABLE tiles (
    id SERIAL PRIMARY KEY,
    project_id INT REFERENCES projects(id) ON DELETE CASCADE,
    material_id INT REFERENCES materials(id) ON DELETE SET NULL,
    size VARCHAR(50),
    color VARCHAR(50),
    texture VARCHAR(255)
);

-- Create a table for materials
CREATE TABLE materials (
    id SERIAL PRIMARY KEY,
    type VARCHAR(100) NOT NULL,
    durability INT,
    cost DECIMAL(10,2)
);

-- Create a table for 3D models
CREATE TABLE model_3d (
    id SERIAL PRIMARY KEY,
    project_id INT REFERENCES projects(id) ON DELETE CASCADE,
    file_path TEXT NOT NULL,
    format VARCHAR(50),
    version VARCHAR(20)
);
