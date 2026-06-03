import React from 'react';
import { scaffolderPlugin } from '@backstage/plugin-scaffolder';
import {
  createScaffolderLayout,
  LayoutTemplate,
} from '@backstage/plugin-scaffolder-react';
import {
  Box,
  Grid,
  Paper,
  Typography,
  Divider,
} from '@material-ui/core';

const PlatformServiceLayoutComponent: LayoutTemplate = ({
  title,
  description,
  properties,
}) => {
  const midpoint = Math.ceil(properties.length / 2);

  return (
    <Box>
      <Paper elevation={1} style={{ padding: 24, marginBottom: 24 }}>
        <Typography variant="h5" gutterBottom>
          {title}
        </Typography>

        {description && (
          <Typography variant="body2" color="textSecondary" paragraph>
            {description}
          </Typography>
        )}

        <Divider style={{ marginBottom: 24 }} />

        <Grid container spacing={3}>
          <Grid item xs={12} md={6}>
            {properties.slice(0, midpoint).map(prop => (
              <Box key={prop.content.key} marginBottom={3}>
                {prop.content}
              </Box>
            ))}
          </Grid>

          <Grid item xs={12} md={6}>
            {properties.slice(midpoint).map(prop => (
              <Box key={prop.content.key} marginBottom={3}>
                {prop.content}
              </Box>
            ))}
          </Grid>
        </Grid>
      </Paper>
    </Box>
  );
};

export const PlatformServiceLayout = scaffolderPlugin.provide(
  createScaffolderLayout({
    name: 'PlatformServiceLayout',
    component: PlatformServiceLayoutComponent,
  }),
);
